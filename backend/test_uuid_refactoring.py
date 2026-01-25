"""
Test Script for UUID Refactoring
Test all key endpoints and verify that UUIDs are working correctly.

Usage:
python test_uuid_refactoring.py

Output:
- Console: Real-time results
- File: test_results_YYYYMMDD_HHMMSS.log
"""

import requests
import json
import sys
from datetime import datetime, date
from typing import Optional, Dict, Any

# Configuration
BASE_URL = "http://localhost:8000"
LOG_FILE = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Colors for console output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class TestRunner:
    def __init__(self):
        self.token: Optional[str] = None
        self.user_id: Optional[str] = None
        self.account_id: Optional[str] = None
        self.category_income_id: Optional[str] = None
        self.category_expense_id: Optional[str] = None
        self.transaction_id: Optional[str] = None
        self.transfer_id: Optional[str] = None
        self.account2_id: Optional[str] = None
        self._test_email: Optional[str] = None  # Initialize here
        
        self.tests_passed = 0
        self.tests_failed = 0
        self.log_lines = []
    
    def log(self, message: str, level: str = "INFO"):
        """Log to console and file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{level}] {message}"
        self.log_lines.append(log_line)
        
        # Console output with colors
        if level == "PASS":
            print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")
        elif level == "FAIL":
            print(f"{Colors.RED}✗ {message}{Colors.RESET}")
        elif level == "INFO":
            print(f"{Colors.BLUE}ℹ {message}{Colors.RESET}")
        elif level == "WARN":
            print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")
        elif level == "HEADER":
            print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BLUE}{message}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
        elif level == "DEBUG":
            print(f"{Colors.YELLOW}  DEBUG: {message}{Colors.RESET}")
        else:
            print(f"  {message}")
    
    def save_log(self):
        """Save log to file."""
        with open(LOG_FILE, 'w') as f:
            f.write('\n'.join(self.log_lines))
        print(f"\n{Colors.BLUE}📄 Log salvato in: {LOG_FILE}{Colors.RESET}")
    
    def is_valid_uuid(self, value: str) -> bool:
        """Check if string is a valid UUID format."""
        import re
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE
        )
        return bool(uuid_pattern.match(str(value)))
    
    def api_call(self, method: str, endpoint: str, data: Dict = None, expected_status: int = None) -> Dict[str, Any]:
        """Make API call and return response."""
        url = f"{BASE_URL}{endpoint}"
        headers = {"Content-Type": "application/json"}
        
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, json=data, headers=headers)
            elif method == "PUT":
                response = requests.put(url, json=data, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unknown method: {method}")
            
            result = {
                "status_code": response.status_code,
                "data": None,
                "error": None
            }
            
            try:
                result["data"] = response.json()
            except:
                result["data"] = response.text
            
            return result
            
        except requests.exceptions.ConnectionError:
            return {"status_code": 0, "data": None, "error": "Connection refused - server not running?"}
        except Exception as e:
            return {"status_code": 0, "data": None, "error": str(e)}
    
    def test(self, name: str, condition: bool, details: str = ""):
        """Record test result."""
        if condition:
            self.tests_passed += 1
            self.log(f"{name} {details}", "PASS")
        else:
            self.tests_failed += 1
            self.log(f"{name} {details}", "FAIL")
    
    # ==================== TEST METHODS ====================
    
    def test_server_health(self):
        """Test if server is running."""
        self.log("Test Server Health", "HEADER")
        
        result = self.api_call("GET", "/")
        
        if result["error"]:
            self.test("Server raggiungibile", False, f"- {result['error']}")
            return False
        
        self.test("Server raggiungibile", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        # Check available routes
        if result["status_code"] == 200:
            self.log("Checking available endpoints...", "INFO")
            
            # Try to get docs
            docs_result = self.api_call("GET", "/docs")
            if docs_result["status_code"] == 200:
                self.log("API docs available at /docs", "INFO")
        
        return result["status_code"] == 200
    
    def test_auth_register(self):
        """Test user registration."""
        self.log("Test Registrazione Utente", "HEADER")
        
        # Generate unique email to avoid conflicts
        unique_email = f"test_{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
        self._test_email = unique_email  # Save email before API call
        
        # Try common auth endpoints
        endpoints_to_try = [
            "/auth/register",
            "/api/auth/register",
            "/api/v1/auth/register",
            "/register"
        ]
        
        result = None
        successful_endpoint = None
        
        for endpoint in endpoints_to_try:
            self.log(f"Trying endpoint: {endpoint}", "DEBUG")
            result = self.api_call("POST", endpoint, {
                "email": unique_email,
                "password": "TestPassword123",
                "full_name": "Test User UUID"
            })
            
            if result["status_code"] in [200, 201]:
                successful_endpoint = endpoint
                break
            elif result["status_code"] != 404:
                # Found endpoint but got different error
                successful_endpoint = endpoint
                break
        
        if successful_endpoint:
            self.log(f"Using endpoint: {successful_endpoint}", "INFO")
        
        self.log(f"Response: {json.dumps(result['data'], indent=2, default=str)}", "DEBUG")
        
        self.test("Registrazione completata", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            user_id = result["data"].get("id")
            self.test("ID utente è UUID valido", self.is_valid_uuid(user_id), f"- ID: {user_id}")
            self.user_id = user_id
            return True
        elif result["status_code"] == 200 and result["data"]:
            # Some APIs return 200 instead of 201
            self.log("Registration returned 200 instead of 201, treating as success", "WARN")
            user_id = result["data"].get("id")
            if user_id:
                self.test("ID utente è UUID valido", self.is_valid_uuid(user_id), f"- ID: {user_id}")
                self.user_id = user_id
                return True
        
        return False
    
    def test_auth_login(self):
        """Test user login."""
        self.log("Test Login", "HEADER")
        
        if not self._test_email:
            self.log("Skip: email di test non disponibile", "WARN")
            return False
        
        # Try common login endpoints
        endpoints_to_try = [
            "/auth/login",
            "/api/auth/login",
            "/api/v1/auth/login",
            "/login",
            "/auth/token"
        ]
        
        result = None
        successful_endpoint = None
        
        for endpoint in endpoints_to_try:
            self.log(f"Trying endpoint: {endpoint}", "DEBUG")
            
            # Try both JSON and form-data formats
            # JSON format
            result = self.api_call("POST", endpoint, {
                "email": self._test_email,
                "password": "TestPassword123"
            })
            
            if result["status_code"] == 200:
                successful_endpoint = endpoint
                break
            
            # Form-data format (OAuth2)
            try:
                url = f"{BASE_URL}{endpoint}"
                response = requests.post(url, data={
                    "username": self._test_email,
                    "password": "TestPassword123"
                })
                if response.status_code == 200:
                    result = {
                        "status_code": response.status_code,
                        "data": response.json(),
                        "error": None
                    }
                    successful_endpoint = f"{endpoint} (form-data)"
                    break
            except:
                pass
        
        if successful_endpoint:
            self.log(f"Using endpoint: {successful_endpoint}", "INFO")
        
        self.test("Login completato", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 200 and result["data"]:
            self.token = result["data"].get("access_token")
            self.test("Token ricevuto", self.token is not None)
            return True
        
        return False
    
    def test_auth_me(self):
        """Test get current user."""
        self.log("Test Get Current User", "HEADER")
        
        if not self.token:
            self.log("Skip: token non disponibile", "WARN")
            return False
        
        # Try common user endpoints
        endpoints_to_try = [
            "/auth/me",
            "/api/auth/me",
            "/api/v1/auth/me",
            "/users/me",
            "/api/users/me"
        ]
        
        result = None
        for endpoint in endpoints_to_try:
            result = self.api_call("GET", endpoint)
            if result["status_code"] == 200:
                self.log(f"Using endpoint: {endpoint}", "INFO")
                break
        
        self.test("GET /auth/me", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 200 and result["data"]:
            user_id = result["data"].get("id")
            self.test("User ID è UUID valido", self.is_valid_uuid(user_id), f"- ID: {user_id}")
            return True
        
        return False
    
    def test_accounts_crud(self):
        """Test account CRUD operations."""
        self.log("Test Account CRUD", "HEADER")
        
        if not self.token:
            self.log("Skip: token non disponibile", "WARN")
            return False
        
        # CREATE Account 1
        result = self.api_call("POST", "/api/v1/accounts", {
            "name": "Conto Test Principale",
            "type": "checking",
            "currency": "EUR",
            "initial_balance": 1000.00,
            "color": "#3B82F6"
        })
        
        self.test("CREATE Account", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            self.account_id = result["data"].get("id")
            user_id = result["data"].get("user_id")
            
            self.test("Account ID è UUID valido", self.is_valid_uuid(self.account_id), f"- ID: {self.account_id}")
            self.test("Account user_id è UUID valido", self.is_valid_uuid(user_id), f"- user_id: {user_id}")
            self.test("Initial balance corretto", float(result["data"].get("initial_balance")) == 1000.0)
            self.test("Current balance corretto", float(result["data"].get("current_balance")) == 1000.0)
        
        # CREATE Account 2 (per transfers)
        result2 = self.api_call("POST", "/api/v1/accounts", {
            "name": "Conto Test Secondario",
            "type": "savings",
            "currency": "EUR",
            "initial_balance": 500.00
        })
        
        if result2["status_code"] == 201 and result2["data"]:
            self.account2_id = result2["data"].get("id")
            self.test("CREATE Account 2", True, f"- ID: {self.account2_id}")
        
        # READ
        if self.account_id:
            result = self.api_call("GET", f"/api/v1/accounts/{self.account_id}")
            self.test("READ Account by UUID", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        # LIST
        result = self.api_call("GET", "/api/v1/accounts")
        self.test("LIST Accounts", result["status_code"] == 200, f"- Count: {len(result['data']) if result['data'] else 0}")
        
        # UPDATE
        if self.account_id:
            result = self.api_call("PUT", f"/api/v1/accounts/{self.account_id}", {
                "name": "Conto Test Aggiornato"
            })
            self.test("UPDATE Account", result["status_code"] == 200, f"- Status: {result['status_code']}")
            
            if result["status_code"] == 200 and result["data"]:
                self.test("Nome aggiornato", result["data"].get("name") == "Conto Test Aggiornato")
        
        return self.account_id is not None
    
    def test_categories_crud(self):
        """Test category CRUD operations."""
        self.log("Test Category CRUD", "HEADER")
        
        if not self.token:
            self.log("Skip: token non disponibile", "WARN")
            return False
        
        # CREATE Income Category
        result = self.api_call("POST", "/api/v1/categories", {
            "name": "Stipendio Test",
            "type": "income",
            "color": "#10B981",
            "icon": "💰"
        })
        
        self.test("CREATE Category (income)", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            self.category_income_id = result["data"].get("id")
            self.test("Category ID è UUID valido", self.is_valid_uuid(self.category_income_id), f"- ID: {self.category_income_id}")
        
        # CREATE Expense Category
        result = self.api_call("POST", "/api/v1/categories", {
            "name": "Spese Test",
            "type": "expense_necessity",
            "color": "#EF4444"
        })
        
        self.test("CREATE Category (expense)", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            self.category_expense_id = result["data"].get("id")
        
        # CREATE Subcategory
        if self.category_income_id:
            result = self.api_call("POST", "/api/v1/categories", {
                "name": "Sottocategoria Test",
                "type": "income",
                "parent_id": self.category_income_id
            })
            
            self.test("CREATE Subcategory con parent_id UUID", result["status_code"] == 201, f"- Status: {result['status_code']}")
            
            if result["status_code"] == 201 and result["data"]:
                parent_id = result["data"].get("parent_id")
                self.test("parent_id è UUID valido", self.is_valid_uuid(parent_id), f"- parent_id: {parent_id}")
        
        # LIST
        result = self.api_call("GET", "/api/v1/categories")
        self.test("LIST Categories", result["status_code"] == 200, f"- Count: {len(result['data']) if result['data'] else 0}")
        
        return self.category_income_id is not None
    
    def test_transactions_crud(self):
        """Test transaction CRUD operations."""
        self.log("Test Transaction CRUD", "HEADER")
        
        if not self.account_id or not self.category_income_id:
            self.log("Skip: mancano account_id o category_id", "WARN")
            return False
        
        # CREATE Income Transaction
        result = self.api_call("POST", "/api/v1/transactions", {
            "account_id": self.account_id,
            "category_id": self.category_income_id,
            "amount": 500.00,
            "date": date.today().isoformat(),
            "description": "Test Income Transaction"
        })
        
        self.test("CREATE Transaction (income)", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            self.transaction_id = result["data"].get("id")
            account_id = result["data"].get("account_id")
            category_id = result["data"].get("category_id")
            user_id = result["data"].get("user_id")
            
            self.test("Transaction ID è UUID valido", self.is_valid_uuid(self.transaction_id), f"- ID: {self.transaction_id}")
            self.test("Transaction account_id è UUID valido", self.is_valid_uuid(account_id))
            self.test("Transaction category_id è UUID valido", self.is_valid_uuid(category_id))
            self.test("Transaction user_id è UUID valido", self.is_valid_uuid(user_id))
            self.test("Transaction type derivato da category", result["data"].get("type") == "income")
        
        # Check balance updated
        result = self.api_call("GET", f"/api/v1/accounts/{self.account_id}")
        if result["status_code"] == 200 and result["data"]:
            current_balance = float(result["data"].get("current_balance"))
            self.test("Balance aggiornato dopo income", current_balance == 1500.0, f"- Balance: {current_balance} (expected: 1500)")
        
        # CREATE Expense Transaction
        result = self.api_call("POST", "/api/v1/transactions", {
            "account_id": self.account_id,
            "category_id": self.category_expense_id,
            "amount": 100.00,
            "date": date.today().isoformat(),
            "description": "Test Expense Transaction"
        })
        
        self.test("CREATE Transaction (expense)", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        # Check balance dopo expense
        result = self.api_call("GET", f"/api/v1/accounts/{self.account_id}")
        if result["status_code"] == 200 and result["data"]:
            current_balance = float(result["data"].get("current_balance"))
            self.test("Balance aggiornato dopo expense", current_balance == 1400.0, f"- Balance: {current_balance} (expected: 1400)")
        
        # LIST
        result = self.api_call("GET", "/api/v1/transactions")
        self.test("LIST Transactions", result["status_code"] == 200, f"- Count: {len(result['data']) if result['data'] else 0}")
        
        return self.transaction_id is not None
    
    def test_transfers_crud(self):
        """Test transfer CRUD operations."""
        self.log("Test Transfer CRUD", "HEADER")
        
        if not self.account_id or not self.account2_id:
            self.log("Skip: mancano account_id", "WARN")
            return False
        
        # CREATE Transfer
        result = self.api_call("POST", "/api/v1/transfers", {
            "from_account_id": self.account_id,
            "to_account_id": self.account2_id,
            "amount": 200.00,
            "type": "generic",
            "date": date.today().isoformat(),
            "description": "Test Transfer"
        })
        
        self.test("CREATE Transfer", result["status_code"] == 201, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 201 and result["data"]:
            self.transfer_id = result["data"].get("id")
            from_account_id = result["data"].get("from_account_id")
            to_account_id = result["data"].get("to_account_id")
            
            self.test("Transfer ID è UUID valido", self.is_valid_uuid(self.transfer_id), f"- ID: {self.transfer_id}")
            self.test("Transfer from_account_id è UUID valido", self.is_valid_uuid(from_account_id))
            self.test("Transfer to_account_id è UUID valido", self.is_valid_uuid(to_account_id))
        
        # Check balances after transfer
        result1 = self.api_call("GET", f"/api/v1/accounts/{self.account_id}")
        result2 = self.api_call("GET", f"/api/v1/accounts/{self.account2_id}")
        
        if result1["status_code"] == 200 and result1["data"]:
            balance1 = float(result1["data"].get("current_balance"))
            self.test("From account balance diminuito", balance1 == 1200.0, f"- Balance: {balance1} (expected: 1200)")
        
        if result2["status_code"] == 200 and result2["data"]:
            balance2 = float(result2["data"].get("current_balance"))
            self.test("To account balance aumentato", balance2 == 700.0, f"- Balance: {balance2} (expected: 700)")
        
        # LIST
        result = self.api_call("GET", "/api/v1/transfers")
        self.test("LIST Transfers", result["status_code"] == 200, f"- Count: {len(result['data']) if result['data'] else 0}")
        
        return self.transfer_id is not None
    
    def test_analytics(self):
        """Test analytics endpoints."""
        self.log("Test Analytics", "HEADER")
        
        if not self.token:
            self.log("Skip: token non disponibile", "WARN")
            return False
        
        # Summary
        result = self.api_call("GET", "/api/v1/analytics/summary")
        self.test("GET /analytics/summary", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        if result["status_code"] == 200 and result["data"]:
            totals = result["data"].get("totals", {})
            self.test("Summary ha income", "income" in totals, f"- Income: {totals.get('income')}")
            self.test("Summary ha expenses", "expenses" in totals, f"- Expenses: {totals.get('expenses')}")
        
        # Monthly Trend
        result = self.api_call("GET", "/api/v1/analytics/monthly-trend")
        self.test("GET /analytics/monthly-trend", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        return True
    
    def test_cleanup(self):
        """Test DELETE operations."""
        self.log("Test Cleanup (DELETE)", "HEADER")
        
        # Delete transfer
        if self.transfer_id:
            result = self.api_call("DELETE", f"/api/v1/transfers/{self.transfer_id}")
            self.test("DELETE Transfer", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        # Delete transaction
        if self.transaction_id:
            result = self.api_call("DELETE", f"/api/v1/transactions/{self.transaction_id}")
            self.test("DELETE Transaction", result["status_code"] == 200, f"- Status: {result['status_code']}")
        
        # Delete categories (skip - they may have transactions)

        # Delete accounts (skip - cascade would delete data)
        
        return True
    
    def run_all_tests(self):
        """Run all tests."""
        self.log("UUID REFACTORING TEST SUITE", "HEADER")
        self.log(f"Base URL: {BASE_URL}")
        self.log(f"Data/Ora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Test sequence
        if not self.test_server_health():
            self.log("Server non raggiungibile. Assicurati che sia in esecuzione.", "FAIL")
            self.print_summary()
            return
        
        # Auth tests
        if self.test_auth_register():
            self.test_auth_login()
            self.test_auth_me()
        else:
            self.log("Registrazione fallita, skipping altri test che richiedono autenticazione", "WARN")
            self.print_summary()
            self.save_log()
            return
        
        # CRUD tests
        self.test_accounts_crud()
        self.test_categories_crud()
        self.test_transactions_crud()
        self.test_transfers_crud()
        self.test_analytics()
        # self.test_cleanup()  # Uncomment to clean test data
        
        self.print_summary()
        self.save_log()
    
    def print_summary(self):
        """Print test summary."""
        self.log("RIEPILOGO TEST", "HEADER")
        
        total = self.tests_passed + self.tests_failed
        
        print(f"\n{Colors.BOLD}Risultati:{Colors.RESET}")
        print(f"  {Colors.GREEN}✓ Passati: {self.tests_passed}{Colors.RESET}")
        print(f"  {Colors.RED}✗ Falliti: {self.tests_failed}{Colors.RESET}")
        print(f"  Totale: {total}")
        
        if self.tests_failed == 0:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 TUTTI I TEST PASSATI! UUID Refactoring OK!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}⚠️ Alcuni test falliti. Controlla il log per dettagli.{Colors.RESET}")


if __name__ == "__main__":
    runner = TestRunner()
    runner.run_all_tests()