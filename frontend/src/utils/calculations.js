/**
 * CALCULATIONS UTILITIES
 * Contiene tutte le funzioni di calcolo per l'applicazione:
 * - Calcolo del saldo dei conti
 * - Calcolo delle statistiche mensili
 * - Filtraggio delle transazioni per periodo
 */

/**
 * Calcola il saldo di un conto specifico
 * @param {number} accountId - ID del conto
 * @param {Array} accounts - Array di tutti i conti
 * @param {Array} transactions - Array di tutte le transazioni
 * @returns {number} - Saldo calcolato
 */
export const calculateAccountBalance = (accountId, accounts, transactions) => {
  // Trova il conto nell'array
  const account = accounts.find(a => a.id === accountId);
  
  // Parte dal saldo iniziale del conto
  let balance = account ? account.initialBalance : 0;

  // Scorre tutte le transazioni e aggiorna il saldo
  transactions.forEach(t => {
    if (t.type === 'transfer') {
      // Se è un trasferimento, toglie dal conto di origine e aggiunge a quello di destinazione
      if (t.fromAccount === accountId) balance -= t.amount;
      if (t.toAccount === accountId) balance += t.amount;
    } else if (t.account === accountId) {
      // Se è una transazione normale sul conto
      if (t.type === 'income') {
        // Le entrate aumentano il saldo
        balance += t.amount;
      } else {
        // Le uscite diminuiscono il saldo
        balance -= t.amount;
      }
    }
  });

  return balance;
};

/**
 * Calcola le statistiche per un insieme di transazioni
 * @param {Array} transactions - Array di transazioni da analizzare
 * @returns {Object} - Oggetto con tutte le statistiche calcolate
 */
export const calculateStats = (transactions) => {
  // Inizializza i contatori
  let income = 0;
  let expenseNecessity = 0;
  let expenseExtra = 0;
  let withdrawals = 0;

  // Somma gli importi per tipo di transazione
  transactions.forEach(t => {
    if (t.type === 'income') income += t.amount;
    else if (t.type === 'expense-necessity') expenseNecessity += t.amount;
    else if (t.type === 'expense-extra') expenseExtra += t.amount;
    else if (t.type === 'withdrawal') withdrawals += t.amount;
  });

  // Calcola i totali
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
 * Filtra le transazioni per un mese e anno specifici
 * @param {Array} transactions - Array di tutte le transazioni
 * @param {number} month - Mese (0-11)
 * @param {number} year - Anno
 * @returns {Array} - Array di transazioni filtrate
 */
export const filterTransactionsByMonth = (transactions, month, year) => {
  return transactions.filter(t => {
    const date = new Date(t.date);
    return date.getMonth() === month && date.getFullYear() === year;
  });
};

/**
 * Calcola i totali per categoria da un array di transazioni
 * @param {Array} transactions - Array di transazioni da analizzare
 * @returns {Object} - Oggetto con categoria come chiave e totale come valore
 */
export const calculateCategoryTotals = (transactions) => {
  const categoryTotals = {};
  
  // Filtra solo le spese (escluse entrate e trasferimenti)
  transactions
    .filter(t => t.type !== 'income' && t.type !== 'transfer')
    .forEach(t => {
      // Somma l'importo per ogni categoria
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
 * Ottiene i dati degli ultimi N mesi per i grafici
 * @param {number} months - Numero di mesi da includere
 * @param {number} currentMonth - Mese corrente (0-11)
 * @param {number} currentYear - Anno corrente
 * @param {Array} transactions - Array di tutte le transazioni
 * @returns {Array} - Array di oggetti con dati mensili
 */
export const getLastMonthsData = (months, currentMonth, currentYear, transactions) => {
  const data = [];

  // Cicla all'indietro partendo dal mese corrente
  for (let i = months - 1; i >= 0; i--) {
    const date = new Date(currentYear, currentMonth - i, 1);
    const month = date.getMonth();
    const year = date.getFullYear();
    
    // Filtra le transazioni per questo mese
    const monthTrans = filterTransactionsByMonth(transactions, month, year);
    
    // Calcola le statistiche per il mese
    const stats = calculateStats(monthTrans);
    
    // Aggiungi i dati all'array
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
 * Ordina le transazioni per data (dalla più recente alla più vecchia)
 * @param {Array} transactions - Array di transazioni da ordinare
 * @returns {Array} - Array di transazioni ordinato
 */
export const sortTransactionsByDate = (transactions) => {
  return [...transactions].sort((a, b) => new Date(b.date) - new Date(a.date));
};
