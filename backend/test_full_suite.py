"""
Full API Test Suite
===================
Copre tutti i moduli dell'applicazione:

  [1]  Auth              — register, login, me
  [2]  Accounts          — CRUD, summary, verify-balances
  [3]  Categories        — CRUD, tree, seed-defaults
  [4]  Transactions      — CRUD, summary, monthly, balance updates
  [5]  Transfers         — CRUD, types, balance updates
  [6]  Analytics         — summary, monthly-trend, by-category, by-account
  [7]  Custom Charts     — CRUD
  [8]  Vacation Settings — GET/PUT maturazione separata
  [9]  Vacation Entries  — validazione weekend, validazione festività
  [10] Vacation Bulk     — skip weekend + festività
  [11] Vacation Balance  — breakdown per tipo + totali aggregati
  [12] Vacation Calendar — festività custom visibile

Uso:
    python test_full_suite.py
    python test_full_suite.py --url http://localhost:8000 --email me@test.com --password secret
    python test_full_suite.py --no-cleanup      # lascia i dati nel DB dopo i test
    python test_full_suite.py --module accounts  # esegue solo un modulo
"""

import argparse
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

# ── Colori terminale ───────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"


# ── Helpers output ─────────────────────────────────────────────────────────────

def ok(msg):     print(f"  {GREEN}✓{RESET} {msg}")
def fail(msg):   print(f"  {RED}✗ {msg}{RESET}")
def info(msg):   print(f"  {YELLOW}→{RESET} {msg}")
def skip(msg):   print(f"  {DIM}⊘ SKIP: {msg}{RESET}")

def _plain(msg: str) -> str:
    """Rimuove i codici ANSI per il log su file."""
    import re
    return re.sub(r'\033\[[0-9;]*m', '', msg)

def section(title):
    print(f"\n{BOLD}{CYAN}── {title} {'─' * (54 - len(title))}{RESET}")


def next_weekday(weekday: int) -> date:
    """Prossima data con il dato weekday (0=Mon … 6=Sun)."""
    today = date.today()
    days_ahead = weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return today + timedelta(days=days_ahead)


def next_national_holiday() -> date:
    """Prossima festività nazionale fissa."""
    fixed = [(1,1),(1,6),(4,25),(5,1),(6,2),(8,15),(11,1),(12,8),(12,25),(12,26)]
    today = date.today()
    year  = today.year
    for month, day in sorted(fixed):
        try:
            d = date(year, month, day)
            if d > today:
                return d
        except ValueError:
            continue
    return date(year + 1, 1, 1)


# ── Core tester ────────────────────────────────────────────────────────────────

class Suite:
    def __init__(self, base_url: str, email: str, password: str, cleanup: bool):
        self.base     = base_url.rstrip("/")
        self.email    = email
        self.password = password
        self.do_cleanup = cleanup
        self.log_lines: list[str] = []
        self.log_path  = Path(f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        self.token    = None
        self.headers  = {}

        # IDs creati durante i test (usati da moduli successivi e per cleanup)
        self.account_id   = None
        self.account2_id  = None
        self.cat_income_id  = None
        self.cat_expense_id = None
        self.transaction_id = None
        self.transfer_id    = None
        self.chart_id       = None
        self.vac_entry_ids  = []
        self.user_holiday_id = None

        self.passed  = 0
        self.failed  = 0
        self.skipped = 0

    # ── HTTP helper ───────────────────────────────────────────────────────────

    def req(self, method: str, path: str, json=None, params=None, expected: int = None):
        """Esegue una chiamata HTTP e ritorna (status_code, body)."""
        url = f"{self.base}{path}"
        try:
            resp = requests.request(
                method, url,
                json=json,
                params=params,
                headers=self.headers,
                timeout=10,
            )
        except requests.exceptions.ConnectionError:
            return 0, {"error": "Connection refused"}
        except Exception as e:
            return 0, {"error": str(e)}

        try:
            body = resp.json()
        except Exception:
            body = resp.text

        return resp.status_code, body

    # ── Assert helpers ────────────────────────────────────────────────────────

    def assert_status(self, status, expected, label):
        if status == expected:
            ok(f"{label} → {status}")
            return True
        fail(f"{label} → atteso {expected}, ricevuto {status}")
        return False

    def assert_field(self, body, field, expected=None):
        if not isinstance(body, dict) or field not in body:
            fail(f"Campo '{field}' mancante")
            return False
        if expected is not None and body[field] != expected:
            fail(f"'{field}' = {body[field]!r}, atteso {expected!r}")
            return False
        ok(f"'{field}' = {body[field]!r}")
        return True

    def _log(self, msg: str):
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_lines.append(f"[{ts}] {_plain(msg)}")

    def check(self, condition: bool, label: str):
        if condition:
            ok(label)
            self._log(f"✓ {label}")
            self.passed += 1
        else:
            fail(label)
            self._log(f"✗ {label}")
            self.failed += 1
        return condition

    def record(self, passed: bool):
        if passed:
            self.passed += 1
        else:
            self.failed += 1

    # =========================================================================
    # [1] AUTH
    # =========================================================================

    def test_auth(self):
        section("[1] Auth")

        # Register
        unique = f"test_{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
        status, body = self.req("POST", "/api/v1/auth/register", {
            "email": unique,
            "password": self.password,
            "full_name": "Test User Suite",
        })
        if not self.check(status == 201, f"POST /auth/register → 201"):
            info(f"body: {body}")
            return False
        self.check("id" in body, "Risposta contiene 'id'")
        self.check(body.get("email") == unique, f"email corretta")

        # Login (usa l'utente appena creato per ottenere il token)
        status, body = self.req("POST", "/api/v1/auth/login/json", {
            "email": unique,
            "password": self.password,
        })
        if not self.check(status == 200, "POST /auth/login/json → 200"):
            info(f"body: {body}")
            return False

        self.token = body.get("access_token")
        self.check(bool(self.token), "access_token presente")
        self.headers = {"Authorization": f"Bearer {self.token}"}

        # GET /me
        status, body = self.req("GET", "/api/v1/auth/me")
        self.check(status == 200, "GET /auth/me → 200")
        self.check("id" in body, "/me ritorna 'id'")
        self.check(body.get("email") == unique, "/me ritorna email corretta")

        return True

    # =========================================================================
    # [2] ACCOUNTS
    # =========================================================================

    def test_accounts(self):
        section("[2] Accounts")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # CREATE principale
        status, body = self.req("POST", "/api/v1/accounts", {
            "name": "Conto Corrente Test",
            "type": "checking",
            "currency": "EUR",
            "initial_balance": 2000.0,
            "color": "#3B82F6",
        })
        if self.check(status == 201, "POST /accounts → 201"):
            self.account_id = body.get("id")
            self.check(bool(self.account_id), "id presente")
            self.check(float(body.get("current_balance", -1)) == 2000.0, "current_balance = 2000")

        # CREATE secondario (per i transfer)
        status, body = self.req("POST", "/api/v1/accounts", {
            "name": "Conto Risparmio Test",
            "type": "savings",
            "currency": "EUR",
            "initial_balance": 500.0,
        })
        if self.check(status == 201, "POST /accounts (secondario) → 201"):
            self.account2_id = body.get("id")

        # LIST
        status, body = self.req("GET", "/api/v1/accounts")
        self.check(status == 200, "GET /accounts → 200")
        self.check(isinstance(body, list) and len(body) >= 2, "Lista contiene ≥ 2 accounts")

        # READ
        if self.account_id:
            status, body = self.req("GET", f"/api/v1/accounts/{self.account_id}")
            self.check(status == 200, f"GET /accounts/{{id}} → 200")

        # UPDATE
        if self.account_id:
            status, body = self.req("PUT", f"/api/v1/accounts/{self.account_id}", {
                "name": "Conto Corrente Aggiornato",
                "color": "#EF4444",
            })
            self.check(status == 200, "PUT /accounts/{id} → 200")
            self.check(body.get("name") == "Conto Corrente Aggiornato", "nome aggiornato")

        # SUMMARY
        status, body = self.req("GET", "/api/v1/accounts/summary")
        self.check(status == 200, "GET /accounts/summary → 200")
        self.check("total_liquid" in body or "accounts" in body or isinstance(body, dict),
                   "summary ha struttura valida")

        # VERIFY BALANCES
        status, body = self.req("GET", "/api/v1/accounts/verify-balances")
        self.check(status == 200, "GET /accounts/verify-balances → 200")

    # =========================================================================
    # [3] CATEGORIES
    # =========================================================================

    def test_categories(self):
        section("[3] Categories")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # SEED DEFAULTS
        status, body = self.req("POST", "/api/v1/categories/seed-defaults")
        self.check(status in (200, 201), "POST /categories/seed-defaults → 200/201")

        # CREATE income
        status, body = self.req("POST", "/api/v1/categories", {
            "name": "Stipendio Test",
            "type": "income",
            "color": "#10B981",
        })
        if self.check(status == 201, "POST /categories (income) → 201"):
            self.cat_income_id = body.get("id")

        # CREATE expense
        status, body = self.req("POST", "/api/v1/categories", {
            "name": "Spese Test",
            "type": "expense_necessity",
            "color": "#EF4444",
        })
        if self.check(status == 201, "POST /categories (expense) → 201"):
            self.cat_expense_id = body.get("id")

        # CREATE subcategory
        if self.cat_income_id:
            status, body = self.req("POST", "/api/v1/categories", {
                "name": "Bonus Test",
                "type": "income",
                "parent_id": self.cat_income_id,
            })
            self.check(status == 201, "POST /categories (subcategory) → 201")
            if status == 201:
                self.check(body.get("parent_id") == self.cat_income_id, "parent_id corretto")

        # LIST
        status, body = self.req("GET", "/api/v1/categories")
        self.check(status == 200, "GET /categories → 200")

        # TREE
        status, body = self.req("GET", "/api/v1/categories/tree")
        self.check(status == 200, "GET /categories/tree → 200")

        # UPDATE
        if self.cat_expense_id:
            status, body = self.req("PUT", f"/api/v1/categories/{self.cat_expense_id}", {
                "name": "Spese Test Aggiornato",
            })
            self.check(status == 200, "PUT /categories/{id} → 200")
            self.check(body.get("name") == "Spese Test Aggiornato", "nome aggiornato")

    # =========================================================================
    # [4] TRANSACTIONS
    # =========================================================================

    def test_transactions(self):
        section("[4] Transactions")

        if not self.token or not self.account_id or not self.cat_income_id:
            skip("mancano account_id o cat_income_id")
            self.skipped += 1
            return

        today = date.today().isoformat()

        # CREATE income
        status, body = self.req("POST", "/api/v1/transactions", {
            "account_id": self.account_id,
            "category_id": self.cat_income_id,
            "amount": 1500.0,
            "date": today,
            "description": "Stipendio test",
        })
        if self.check(status == 201, "POST /transactions (income) → 201"):
            self.transaction_id = body.get("id")
            self.check(body.get("type") == "income", "type derivato da categoria = income")

        # Verifica balance aggiornato: 2000 + 1500 = 3500
        status, body = self.req("GET", f"/api/v1/accounts/{self.account_id}")
        if status == 200:
            bal = float(body.get("current_balance", -1))
            self.check(bal == 3500.0, f"Balance aggiornato dopo income: {bal} == 3500")

        # CREATE expense
        if self.cat_expense_id:
            status, body = self.req("POST", "/api/v1/transactions", {
                "account_id": self.account_id,
                "category_id": self.cat_expense_id,
                "amount": 200.0,
                "date": today,
                "description": "Spesa test",
            })
            self.check(status == 201, "POST /transactions (expense) → 201")

            # Balance: 3500 - 200 = 3300
            status, body = self.req("GET", f"/api/v1/accounts/{self.account_id}")
            if status == 200:
                bal = float(body.get("current_balance", -1))
                self.check(bal == 3300.0, f"Balance aggiornato dopo expense: {bal} == 3300")

        # LIST
        status, body = self.req("GET", "/api/v1/transactions")
        self.check(status == 200, "GET /transactions → 200")
        self.check(isinstance(body, list), "Risposta è lista")

        # SUMMARY
        status, body = self.req("GET", "/api/v1/transactions/summary")
        self.check(status == 200, "GET /transactions/summary → 200")

        # MONTHLY
        year  = date.today().year
        month = date.today().month
        status, body = self.req("GET", f"/api/v1/transactions/monthly/{year}/{month}")
        self.check(status == 200, f"GET /transactions/monthly/{year}/{month} → 200")

        # READ singola
        if self.transaction_id:
            status, body = self.req("GET", f"/api/v1/transactions/{self.transaction_id}")
            self.check(status == 200, "GET /transactions/{id} → 200")

        # UPDATE
        if self.transaction_id:
            status, body = self.req("PUT", f"/api/v1/transactions/{self.transaction_id}", {
                "description": "Stipendio test aggiornato",
                "notes": "Nota test",
            })
            self.check(status == 200, "PUT /transactions/{id} → 200")
            self.check(body.get("description") == "Stipendio test aggiornato", "descrizione aggiornata")

    # =========================================================================
    # [5] TRANSFERS
    # =========================================================================

    def test_transfers(self):
        section("[5] Transfers")

        if not self.token or not self.account_id or not self.account2_id:
            skip("mancano account_id / account2_id")
            self.skipped += 1
            return

        # TYPES
        status, body = self.req("GET", "/api/v1/transfers/types")
        self.check(status == 200, "GET /transfers/types → 200")
        self.check(isinstance(body, list) and len(body) > 0, "Lista types non vuota")

        # CREATE
        status, body = self.req("POST", "/api/v1/transfers", {
            "from_account_id": self.account_id,
            "to_account_id": self.account2_id,
            "amount": 300.0,
            "type": "savings",
            "date": date.today().isoformat(),
            "description": "Trasferimento test",
        })
        if self.check(status == 201, "POST /transfers → 201"):
            self.transfer_id = body.get("id")
            self.check(bool(self.transfer_id), "id presente")

        # Verifica balance: from 3300-300=3000, to 500+300=800
        status, body1 = self.req("GET", f"/api/v1/accounts/{self.account_id}")
        status, body2 = self.req("GET", f"/api/v1/accounts/{self.account2_id}")
        if body1 and body2:
            bal1 = float(body1.get("current_balance", -1))
            bal2 = float(body2.get("current_balance", -1))
            self.check(bal1 == 3000.0, f"From balance dopo transfer: {bal1} == 3000")
            self.check(bal2 == 800.0,  f"To balance dopo transfer:   {bal2} == 800")

        # LIST
        status, body = self.req("GET", "/api/v1/transfers")
        self.check(status == 200, "GET /transfers → 200")

        # READ
        if self.transfer_id:
            status, body = self.req("GET", f"/api/v1/transfers/{self.transfer_id}")
            self.check(status == 200, "GET /transfers/{id} → 200")

        # UPDATE
        if self.transfer_id:
            status, body = self.req("PUT", f"/api/v1/transfers/{self.transfer_id}", {
                "description": "Trasferimento aggiornato",
            })
            self.check(status == 200, "PUT /transfers/{id} → 200")

        # STATISTICS
        status, body = self.req("GET", "/api/v1/transfers/statistics")
        self.check(status == 200, "GET /transfers/statistics → 200")

    # =========================================================================
    # [6] ANALYTICS
    # =========================================================================

    def test_analytics(self):
        section("[6] Analytics")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # SUMMARY
        status, body = self.req("GET", "/api/v1/analytics/summary")
        self.check(status == 200, "GET /analytics/summary → 200")
        if isinstance(body, dict):
            self.check("totals" in body or "income" in body or len(body) > 0,
                       "Summary ha contenuto")

        # MONTHLY TREND
        status, body = self.req("GET", "/api/v1/analytics/monthly-trend")
        self.check(status == 200, "GET /analytics/monthly-trend → 200")

        # BY CATEGORY
        status, body = self.req("GET", "/api/v1/analytics/by-category")
        self.check(status == 200, "GET /analytics/by-category → 200")

        # BY ACCOUNT
        status, body = self.req("GET", "/api/v1/analytics/by-account")
        self.check(status == 200, "GET /analytics/by-account → 200")

        # DAILY BREAKDOWN
        status, body = self.req("GET", "/api/v1/analytics/daily-breakdown")
        self.check(status == 200, "GET /analytics/daily-breakdown → 200")

    # =========================================================================
    # [7] CUSTOM CHARTS
    # =========================================================================

    def test_custom_charts(self):
        section("[7] Custom Charts")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # CREATE
        status, body = self.req("POST", "/api/v1/custom-charts", {
            "name": "Grafico Test",
            "chart_type": "bar",
            "config": {"dataKey": "amount", "color": "#3B82F6"},
        })
        if self.check(status == 201, "POST /custom-charts → 201"):
            self.chart_id = body.get("id")
            self.check(bool(self.chart_id), "id presente")

        # LIST
        status, body = self.req("GET", "/api/v1/custom-charts")
        self.check(status == 200, "GET /custom-charts → 200")

        # READ
        if self.chart_id:
            status, body = self.req("GET", f"/api/v1/custom-charts/{self.chart_id}")
            self.check(status == 200, "GET /custom-charts/{id} → 200")

        # UPDATE
        if self.chart_id:
            status, body = self.req("PUT", f"/api/v1/custom-charts/{self.chart_id}", {
                "name": "Grafico Test Aggiornato",
            })
            self.check(status == 200, "PUT /custom-charts/{id} → 200")
            self.check(body.get("name") == "Grafico Test Aggiornato", "nome aggiornato")

    # =========================================================================
    # [8] VACATION — SETTINGS
    # =========================================================================

    def test_vacation_settings(self):
        section("[8] Vacation Settings — maturazione separata")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # GET (crea defaults al primo accesso)
        status, body = self.req("GET", "/api/v1/vacation/settings")
        self.check(status == 200, "GET /vacation/settings → 200")
        for field in ["ferie_days_per_month", "rol_hours_per_month", "permessi_hours_per_month"]:
            self.check(field in body, f"Campo '{field}' presente")

        # PUT — aggiorna i tre tassi separatamente
        status, body = self.req("PUT", "/api/v1/vacation/settings", {
            "ferie_days_per_month": 2.0,
            "rol_hours_per_month": 3.5,
            "permessi_hours_per_month": 9.5,
        })
        self.check(status == 200, "PUT /vacation/settings → 200")
        self.check(body.get("ferie_days_per_month") == 2.0,   "ferie_days_per_month aggiornato")
        self.check(body.get("rol_hours_per_month") == 3.5,    "rol_hours_per_month aggiornato")
        self.check(body.get("permessi_hours_per_month") == 9.5, "permessi_hours_per_month aggiornato")

        # Verifica indipendenza: aggiorna solo uno, gli altri rimangono invariati
        status, body = self.req("PUT", "/api/v1/vacation/settings", {
            "ferie_days_per_month": 1.83,
        })
        self.check(body.get("ferie_days_per_month") == 1.83, "ferie_days_per_month ripristinato a 1.83")
        self.check(body.get("rol_hours_per_month") == 3.5,   "rol_hours_per_month invariato dopo update parziale")

        # Ripristina defaults completi
        self.req("PUT", "/api/v1/vacation/settings", {
            "rol_hours_per_month": 2.67,
            "permessi_hours_per_month": 8.67,
        })
        info("Settings ripristinati ai valori default")

    # =========================================================================
    # [9] VACATION ENTRIES — validazioni
    # =========================================================================

    def test_vacation_entries_validation(self):
        section("[9] Vacation Entries — validazione weekend e festività")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        # Weekend → 400
        saturday = next_weekday(5)
        info(f"Tentativo ferie su sabato: {saturday}")
        status, body = self.req("POST", "/api/v1/vacation/entries", {
            "date": str(saturday),
            "entry_type": "ferie",
        })
        if self.check(status == 400, f"POST /vacation/entries ({saturday} sabato) → 400"):
            info(f"  Messaggio: {body.get('detail', '')}")

        # Festività nazionale → 400
        holiday = next_national_holiday()
        info(f"Tentativo ferie su festività: {holiday}")
        status, body = self.req("POST", "/api/v1/vacation/entries", {
            "date": str(holiday),
            "entry_type": "ferie",
        })
        if self.check(status == 400, f"POST /vacation/entries ({holiday} festività) → 400"):
            info(f"  Messaggio: {body.get('detail', '')}")

        # ROL senza hours → 400 (validazione schema)
        workday = next_weekday(0)  # prossimo lunedì
        status, body = self.req("POST", "/api/v1/vacation/entries", {
            "date": str(workday),
            "entry_type": "rol",
            # hours mancante — deve fallire
        })
        self.check(status == 422, "POST /vacation/entries (ROL senza hours) → 422")

    # =========================================================================
    # [10] VACATION BULK — skip festività
    # =========================================================================

    def test_vacation_bulk(self):
        section("[10] Vacation Bulk — skip weekend + festività")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        year = date.today().year
        # Range che include il 25 aprile (Festa della Liberazione) e il weekend
        start = date(year, 4, 22)  # martedì
        end   = date(year, 4, 27)  # domenica
        info(f"Range: {start} → {end} (include 25/04 e weekend)")

        status, body = self.req("POST", "/api/v1/vacation/entries/bulk", {
            "start_date": str(start),
            "end_date": str(end),
            "entry_type": "ferie",
            "skip_weekends": True,
            "skip_holidays": True,
        })

        if not self.check(status == 201, "POST /vacation/entries/bulk → 201"):
            info(f"body: {body}")
            return

        dates = [e["date"] for e in body]
        info(f"Date inserite: {dates}")

        april25 = str(date(year, 4, 25))
        self.check(april25 not in dates, f"25 aprile ({april25}) correttamente escluso")

        weekend_found = [d for d in dates if date.fromisoformat(d).weekday() >= 5]
        self.check(len(weekend_found) == 0, f"Nessun weekend nelle entries (trovati: {weekend_found})")

        self.check(len(body) > 0, f"Almeno una entry inserita ({len(body)} totali)")
        self.vac_entry_ids.extend([e["id"] for e in body])

    # =========================================================================
    # [11] VACATION BALANCE
    # =========================================================================

    def test_vacation_balance(self):
        section("[11] Vacation Balance — breakdown + totali aggregati")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        status, body = self.req("GET", "/api/v1/vacation/balance")
        self.check(status == 200, "GET /vacation/balance → 200")

        # Totali aggregati
        for field in ["total_hours_accrued", "total_hours_used",
                      "total_hours_available", "total_days_available"]:
            self.check(field in body, f"Campo aggregato '{field}' presente")

        # Breakdown per tipo: deve avere 3 voci
        breakdown = body.get("breakdown", [])
        self.check(len(breakdown) == 3, f"Breakdown ha 3 voci (trovate: {len(breakdown)})")

        if len(breakdown) == 3:
            types_found = [b["type"] for b in breakdown]
            self.check(
                set(types_found) == {"ferie", "rol", "permesso"},
                f"Tipi nel breakdown: {types_found}",
            )
            for b in breakdown:
                for sub in ["hours_accrued", "hours_used", "hours_available"]:
                    self.check(sub in b, f"breakdown[{b['type']}].{sub} presente")

        # Coerenza numerica
        total_available = body.get("total_hours_available", -1)
        self.check(total_available >= 0, f"total_hours_available ≥ 0 (= {total_available})")

        # Con parametri anno/mese
        year  = date.today().year
        month = date.today().month
        status, body = self.req("GET", "/api/v1/vacation/balance",
                                params={"year": year, "month": month})
        self.check(status == 200, f"GET /vacation/balance?year={year}&month={month} → 200")

    # =========================================================================
    # [12] VACATION CALENDAR — festività custom
    # =========================================================================

    def test_vacation_calendar(self):
        section("[12] Vacation Calendar — festività custom visibile")

        if not self.token:
            skip("token non disponibile")
            self.skipped += 1
            return

        today = date.today()
        target_year  = today.year if today.month < 12 else today.year + 1
        target_month = today.month + 1 if today.month < 12 else 1

        custom_day  = 10
        custom_name = "Patrono Test"
        info(f"Creazione user-holiday: {custom_name} il {custom_day}/{target_month}")

        # Crea user-holiday
        status, body = self.req("POST", "/api/v1/vacation/user-holidays", {
            "day": custom_day,
            "month": target_month,
            "name": custom_name,
            "recurring": True,
        })
        if not self.check(status == 201, "POST /vacation/user-holidays → 201"):
            return
        self.user_holiday_id = body.get("id")

        # GET user-holidays
        status, body = self.req("GET", "/api/v1/vacation/user-holidays")
        self.check(status == 200, "GET /vacation/user-holidays → 200")
        self.check(isinstance(body, list) and len(body) >= 1, "Lista user-holidays non vuota")

        # GET calendar
        status, body = self.req("GET", f"/api/v1/vacation/calendar/{target_year}/{target_month}")
        if not self.check(status == 200,
                          f"GET /vacation/calendar/{target_year}/{target_month} → 200"):
            return

        days = body.get("days", [])
        day10 = next((d for d in days if d["day_number"] == custom_day), None)

        self.check(day10 is not None, f"Giorno {custom_day} presente nel calendario")
        if day10:
            self.check(day10.get("is_user_holiday") is True,
                       f"Giorno {custom_day}: is_user_holiday = True")
            self.check(day10.get("user_holiday_name") == custom_name,
                       f"Giorno {custom_day}: user_holiday_name = '{custom_name}'")

        # Holidays nazionali
        year = date.today().year
        status, body = self.req("GET", f"/api/v1/vacation/holidays/{year}")
        self.check(status == 200, f"GET /vacation/holidays/{year} → 200")
        self.check(isinstance(body, list) and len(body) >= 10,
                   f"Almeno 10 festività nazionali ({len(body) if isinstance(body, list) else 0} trovate)")

        # Bridge opportunities
        status, body = self.req("GET", f"/api/v1/vacation/bridges/{year}")
        self.check(status == 200, f"GET /vacation/bridges/{year} → 200")
        self.check(isinstance(body, list), "Risposta bridges è lista")

    # =========================================================================
    # CLEANUP
    # =========================================================================

    def cleanup(self):
        section("Cleanup")

        if not self.do_cleanup:
            info("--no-cleanup specificato, dati lasciati nel DB")
            return

        for eid in self.vac_entry_ids:
            s, _ = self.req("DELETE", f"/api/v1/vacation/entries/{eid}")
            ok(f"Vacation entry {eid[:8]}… eliminata") if s == 204 else info(f"Entry {eid[:8]}… skip ({s})")

        if self.user_holiday_id:
            s, _ = self.req("DELETE", f"/api/v1/vacation/user-holidays/{self.user_holiday_id}")
            ok(f"User-holiday eliminata") if s == 204 else info(f"User-holiday skip ({s})")

        if self.chart_id:
            s, _ = self.req("DELETE", f"/api/v1/custom-charts/{self.chart_id}")
            ok(f"Custom chart eliminato") if s == 204 else info(f"Chart skip ({s})")

        if self.transfer_id:
            s, _ = self.req("DELETE", f"/api/v1/transfers/{self.transfer_id}")
            ok(f"Transfer eliminato") if s in (200, 204) else info(f"Transfer skip ({s})")

        if self.transaction_id:
            s, _ = self.req("DELETE", f"/api/v1/transactions/{self.transaction_id}")
            ok(f"Transaction eliminata") if s in (200, 204) else info(f"Transaction skip ({s})")

        # Account: elimina solo quelli di test (cascade elimina il resto)
        for acc_id in filter(None, [self.account2_id, self.account_id]):
            s, _ = self.req("DELETE", f"/api/v1/accounts/{acc_id}")
            ok(f"Account {acc_id[:8]}… eliminato") if s == 204 else info(f"Account skip ({s})")

    # =========================================================================
    # RUN
    # =========================================================================

    def run(self, only_module: str = None):
        print(f"\n{BOLD}{'='*60}")
        print("  BUDGET APP — Full API Test Suite")
        print(f"  Target : {self.base}")
        print(f"  Data   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}{RESET}")

        # Verifica server attivo
        s, _ = self.req("GET", "/")
        if s == 0:
            print(f"\n{RED}{BOLD}Server non raggiungibile su {self.base}{RESET}")
            sys.exit(1)

        modules = {
            "auth":               self.test_auth,
            "accounts":           self.test_accounts,
            "categories":         self.test_categories,
            "transactions":       self.test_transactions,
            "transfers":          self.test_transfers,
            "analytics":          self.test_analytics,
            "custom_charts":      self.test_custom_charts,
            "vacation_settings":  self.test_vacation_settings,
            "vacation_entries":   self.test_vacation_entries_validation,
            "vacation_bulk":      self.test_vacation_bulk,
            "vacation_balance":   self.test_vacation_balance,
            "vacation_calendar":  self.test_vacation_calendar,
        }

        if only_module:
            if only_module not in modules:
                print(f"{RED}Modulo '{only_module}' non trovato. Disponibili: {', '.join(modules)}{RESET}")
                sys.exit(1)
            # Per moduli non-auth abbiamo bisogno del token
            if only_module != "auth":
                self.test_auth()
            modules[only_module]()
        else:
            for fn in modules.values():
                fn()

        self.cleanup()
        self._summary()

    def _summary(self):
        total = self.passed + self.failed
        print(f"\n{BOLD}{'='*60}")
        print(f"  RIEPILOGO FINALE")
        print(f"{'='*60}{RESET}")
        print(f"  {GREEN}✓ Passati : {self.passed}{RESET}")
        print(f"  {RED}✗ Falliti : {self.failed}{RESET}")
        if self.skipped:
            print(f"  {DIM}⊘ Saltati : {self.skipped}{RESET}")
        print(f"  Totale   : {total}")

        if self.failed == 0:
            print(f"\n{GREEN}{BOLD}  🎉 TUTTI I TEST PASSATI!{RESET}\n")
        else:
            print(f"\n{RED}{BOLD}  ⚠️  {self.failed} test falliti — controlla l'output sopra.{RESET}\n")

        # Salva log su file
        self.log_lines.append("")
        self.log_lines.append(f"{'='*60}")
        self.log_lines.append(f"Passati: {self.passed}  Falliti: {self.failed}  Saltati: {self.skipped}  Totale: {total}")
        self.log_path.write_text("\n".join(self.log_lines), encoding="utf-8")
        print(f"{CYAN}📄 Log salvato in: {self.log_path}{RESET}\n")

        sys.exit(0 if self.failed == 0 else 1)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Budget App — Full API Test Suite")
    parser.add_argument("--url",        default="http://localhost:8000", help="Base URL del server")
    parser.add_argument("--email",      default="test@example.com",      help="Email utente (deve esistere o verrà creato)")
    parser.add_argument("--password",   default="Testpassword123!",       help="Password utente")
    parser.add_argument("--no-cleanup", action="store_true",              help="Non eliminare i dati creati durante i test")
    parser.add_argument("--module",     default=None,
                        help="Esegui solo un modulo specifico: auth, accounts, categories, "
                             "transactions, transfers, analytics, custom_charts, "
                             "vacation_settings, vacation_entries, vacation_bulk, "
                             "vacation_balance, vacation_calendar")
    args = parser.parse_args()

    suite = Suite(
        base_url=args.url,
        email=args.email,
        password=args.password,
        cleanup=not args.no_cleanup,
    )
    suite.run(only_module=args.module)
