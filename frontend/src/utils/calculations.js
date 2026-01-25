/**
 * CALCULATIONS UTILITIES
 * Contains all the calculation functions for the application:
 * - Account balance calculation
 * - Monthly statistics calculation
 * - Transaction filtering by period
 */

/**
 * Calculate the balance of a specific account
 * @param {number} accountId - Account ID
 * @param {Array} accounts - Array of all accounts
 * @param {Array} transactions - Array of all transactions
 * @returns {number} - Balance calculated
 */
export const calculateAccountBalance = (accountId, accounts, transactions) => {
  // Find the account in the array
  const account = accounts.find(a => a.id === accountId);
  
  // It starts from the initial balance of the account
  let balance = account ? account.initialBalance : 0;

  // Scroll through all transactions and update your balance
  transactions.forEach(t => {
    if (t.type === 'transfer') {
      // If it's a transfer, it deducts from the source account and adds to the destination account.
      if (t.fromAccount === accountId) balance -= t.amount;
      if (t.toAccount === accountId) balance += t.amount;
    } else if (t.account === accountId) {
      // If it is a normal transaction on the account
      if (t.type === 'income') {
        // Revenue increases the balance
        balance += t.amount;
      } else {
        // Expenditures decrease the balance
        balance -= t.amount;
      }
    }
  });

  return balance;
};

/**
 * Calculate statistics for a set of transactions
 * @param {Array} transactions - Array of transactions to analyze
 * @returns {Object} - Object with all statistics calculated
 */
export const calculateStats = (transactions) => {
  // Initialize the counters
  let income = 0;
  let expenseNecessity = 0;
  let expenseExtra = 0;
  let withdrawals = 0;

  // Adds the amounts by transaction type
  transactions.forEach(t => {
    if (t.type === 'income') income += t.amount;
    else if (t.type === 'expense-necessity') expenseNecessity += t.amount;
    else if (t.type === 'expense-extra') expenseExtra += t.amount;
    else if (t.type === 'withdrawal') withdrawals += t.amount;
  });

  // Calculate the totals
  const totalExpenses = expenseNecessity + expenseExtra + withdrawals;
  const net = income - totalExpenses;

  return {
    income,
    expenseNecessity,
    expenseExtra,
    withdrawals,
    totalExpenses,
    net
  };
};

/**
 * Filter transactions for a specific month and year
 * @param {Array} transactions - Array of all transactions
 * @param {number} month - Month (0-11)
 * @param {number} year - Year
 * @returns {Array} - Array of filtered transactions
 */
export const filterTransactionsByMonth = (transactions, month, year) => {
  return transactions.filter(t => {
    const date = new Date(t.date);
    return date.getMonth() === month && date.getFullYear() === year;
  });
};

/**
 * Calculate category totals from an array of transactions
 * @param {Array} transactions - Array of transactions to analyze
 * @returns {Object} - Object with category as key and total as value
 */
export const calculateCategoryTotals = (transactions) => {
  const categoryTotals = {};
  
  // Filter expenses only (excluding income and transfers)
  transactions
    .filter(t => t.type !== 'income' && t.type !== 'transfer')
    .forEach(t => {
      // Add the amount for each category
      categoryTotals[t.category] = (categoryTotals[t.category] || 0) + t.amount;
    });

  return categoryTotals;
};

/**
 * Calcola il patrimonio totale sommando tutti i saldi dei conti
 * @param {Array} accounts - Array di tutti i conti
 * @param {Array} transactions - Array di tutte le transazioni
 * @returns {number} - Patrimonio totale
 */
export const calculateTotalBalance = (accounts, transactions) => {
  return accounts.reduce((sum, acc) => {
    return sum + calculateAccountBalance(acc.id, accounts, transactions);
  }, 0);
};

/**
 * Gets data from the last N months for charts
 * @param {number} months - Number of months to include
 * @param {number} currentMonth - Current Month (0-11)
 * @param {number} currentYear - Current Year
 * @param {Array} transactions - Array of all transactions
 * @returns {Array} - Array of objects with monthly data
 */
export const getLastMonthsData = (months, currentMonth, currentYear, transactions) => {
  const data = [];

  // Cycle backwards from the current month
  for (let i = months - 1; i >= 0; i--) {
    const date = new Date(currentYear, currentMonth - i, 1);
    const month = date.getMonth();
    const year = date.getFullYear();
    
    // Filter transactions for this month
    const monthTrans = filterTransactionsByMonth(transactions, month, year);
    
   // Calculate statistics for the month
    const stats = calculateStats(monthTrans);
    
    // Add data to the array
    data.push({
      label: date.toLocaleDateString('it-IT', { month: 'short', year: '2-digit' }),
      date: date,
      income: stats.income,
      expenses: stats.totalExpenses,
      net: stats.net,
      transactions: monthTrans
    });
  }

  return data;
};

/**
 * Sort transactions by date (newest to oldest)
 * @param {Array} transactions - Array of transactions to sort
 * @returns {Array} - Sorted array of transactions
 */
export const sortTransactionsByDate = (transactions) => {
  return [...transactions].sort((a, b) => new Date(b.date) - new Date(a.date));
};
