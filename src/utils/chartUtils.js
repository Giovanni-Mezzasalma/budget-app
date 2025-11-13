/**
 * CHART UTILITIES
 * Contiene funzioni di utilità per la generazione dei dati dei grafici personalizzati
 */

import { filterTransactionsByMonth } from './calculations';

/**
 * Ottiene i dati per un periodo specifico basato sulla configurazione
 * @param {string} period - Tipo di periodo ('last3', 'last6', 'last12', 'currentYear', 'custom')
 * @param {Object} options - Opzioni aggiuntive (startDate, endDate per periodo custom)
 * @param {Array} transactions - Array di tutte le transazioni
 * @returns {Array} - Array di dati mensili per il periodo specificato
 */
export const getPeriodData = (period, options, transactions) => {
  const data = [];
  let startDate, endDate, months;

  const currentMonth = new Date().getMonth();
  const currentYear = new Date().getFullYear();

  // Determina il numero di mesi e le date in base al periodo selezionato
  switch (period) {
    case 'last3':
      months = 3;
      break;
    case 'last6':
      months = 6;
      break;
    case 'last12':
      months = 12;
      break;
    case 'currentYear':
      // Anno corrente: da gennaio a dicembre
      startDate = new Date(currentYear, 0, 1);
      endDate = new Date(currentYear, 11, 31);
      months = 12;
      break;
    case 'custom':
      // Periodo personalizzato: usa le date fornite nelle opzioni
      if (options.startDate && options.endDate) {
        const start = new Date(options.startDate + '-01');
        const end = new Date(options.endDate + '-01');
        months = (end.getFullYear() - start.getFullYear()) * 12 + 
                (end.getMonth() - start.getMonth()) + 1;
        startDate = start;
      } else {
        months = 6; // Default se le date non sono fornite
      }
      break;
    default:
      months = 6;
  }

  // Genera i dati per ogni mese del periodo
  for (let i = months - 1; i >= 0; i--) {
    const date = startDate ? 
      new Date(startDate.getFullYear(), startDate.getMonth() + (months - 1 - i), 1) :
      new Date(currentYear, currentMonth - i, 1);
    
    const month = date.getMonth();
    const year = date.getFullYear();
    
    // Filtra le transazioni per questo mese
    const monthTrans = filterTransactionsByMonth(transactions, month, year);

    data.push({
      label: date.toLocaleDateString('it-IT', { month: 'short', year: '2-digit' }),
      date: date,
      transactions: monthTrans
    });
  }

  return data;
};

/**
 * Genera i dati per un grafico di panoramica (entrate/uscite/netto)
 * @param {Array} periodData - Dati mensili del periodo
 * @param {Object} config - Configurazione del grafico
 * @returns {Object} - Dati formattati per Chart.js
 */
export const getOverviewData = (periodData, config) => {
  const datasets = [];
  
  // Dataset per le entrate
  if (config.options.showIncome) {
    datasets.push({
      label: 'Entrate',
      data: periodData.map(p => {
        return p.transactions
          .filter(t => t.type === 'income')
          .reduce((sum, t) => sum + t.amount, 0);
      }),
      borderColor: '#10b981',
      backgroundColor: config.type === 'bar' ? '#10b981' : 'rgba(16, 185, 129, 0.2)',
      tension: 0.4
    });
  }

  // Dataset per le uscite totali
  if (config.options.showExpenses) {
    datasets.push({
      label: 'Uscite',
      data: periodData.map(p => {
        return p.transactions
          .filter(t => t.type !== 'income' && t.type !== 'transfer')
          .reduce((sum, t) => sum + t.amount, 0);
      }),
      borderColor: '#ef4444',
      backgroundColor: config.type === 'bar' ? '#ef4444' : 'rgba(239, 68, 68, 0.2)',
      tension: 0.4
    });
  }

  // Dataset per le spese di necessità
  if (config.options.showNecessity) {
    datasets.push({
      label: 'Spese Necessità',
      data: periodData.map(p => {
        return p.transactions
          .filter(t => t.type === 'expense-necessity')
          .reduce((sum, t) => sum + t.amount, 0);
      }),
      borderColor: '#f59e0b',
      backgroundColor: config.type === 'bar' ? '#f59e0b' : 'rgba(245, 158, 11, 0.2)',
      tension: 0.4
    });
  }

  // Dataset per le spese extra
  if (config.options.showExtra) {
    datasets.push({
      label: 'Spese Extra',
      data: periodData.map(p => {
        return p.transactions
          .filter(t => t.type === 'expense-extra')
          .reduce((sum, t) => sum + t.amount, 0);
      }),
      borderColor: '#8b5cf6',
      backgroundColor: config.type === 'bar' ? '#8b5cf6' : 'rgba(139, 92, 246, 0.2)',
      tension: 0.4
    });
  }

  // Dataset per il netto
  if (config.options.showNet) {
    datasets.push({
      label: 'Netto',
      data: periodData.map(p => {
        const income = p.transactions.filter(t => t.type === 'income')
          .reduce((sum, t) => sum + t.amount, 0);
        const expenses = p.transactions.filter(t => t.type !== 'income' && t.type !== 'transfer')
          .reduce((sum, t) => sum + t.amount, 0);
        return income - expenses;
      }),
      borderColor: '#3b82f6',
      backgroundColor: config.type === 'bar' ? '#3b82f6' : 'rgba(59, 130, 246, 0.2)',
      tension: 0.4
    });
  }

  return {
    labels: periodData.map(p => p.label),
    datasets: datasets
  };
};

/**
 * Genera i dati per un grafico delle categorie
 * @param {Array} periodData - Dati mensili del periodo
 * @param {Object} config - Configurazione del grafico
 * @returns {Object} - Dati formattati per Chart.js
 */
export const getCategoriesData = (periodData, config) => {
  const categoryTotals = {};
  
  // Somma le spese per categoria in tutto il periodo
  periodData.forEach(p => {
    p.transactions.filter(t => t.type !== 'income' && t.type !== 'transfer').forEach(t => {
      categoryTotals[t.category] = (categoryTotals[t.category] || 0) + t.amount;
    });
  });

  // Ordina le categorie per importo decrescente e prende le prime 10
  const sorted = Object.entries(categoryTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  return {
    labels: sorted.map(([cat]) => cat),
    datasets: [{
      label: 'Spesa Totale',
      data: sorted.map(([_, amount]) => amount),
      backgroundColor: [
        '#667eea', '#764ba2', '#f093fb', '#4facfe',
        '#43e97b', '#fa709a', '#fee140', '#30cfd0',
        '#a8edea', '#fed6e3'
      ]
    }]
  };
};

/**
 * Genera i dati per un grafico dei conti
 * @param {Array} periodData - Dati mensili del periodo
 * @param {Object} config - Configurazione del grafico
 * @param {Array} accounts - Array di tutti i conti
 * @returns {Object} - Dati formattati per Chart.js
 */
export const getAccountsData = (periodData, config, accounts) => {
  const selectedAccounts = config.options.selectedAccounts || accounts.map(a => a.id);
  const datasets = [];

  // Colori per i diversi conti
  const colors = ['#667eea', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899'];

  selectedAccounts.forEach((accId, index) => {
    const account = accounts.find(a => a.id === accId);
    if (!account) return;

    datasets.push({
      label: account.name,
      data: periodData.map(p => {
        let balance = 0;
        // Calcola il saldo mensile per questo conto
        p.transactions.forEach(t => {
          if (t.type === 'transfer') {
            if (t.fromAccount === accId) balance -= t.amount;
            if (t.toAccount === accId) balance += t.amount;
          } else if (t.account === accId) {
            if (t.type === 'income') balance += t.amount;
            else balance -= t.amount;
          }
        });
        return balance;
      }),
      borderColor: colors[index % colors.length],
      backgroundColor: config.type === 'bar' ? colors[index % colors.length] : 
        `${colors[index % colors.length]}33`,
      tension: 0.4
    });
  });

  return {
    labels: periodData.map(p => p.label),
    datasets: datasets
  };
};

/**
 * Genera i dati per un grafico di dettaglio di una categoria specifica
 * @param {Array} periodData - Dati mensili del periodo
 * @param {Object} config - Configurazione del grafico
 * @returns {Object} - Dati formattati per Chart.js
 */
export const getCategoryDetailData = (periodData, config) => {
  const category = config.options.category;
  
  return {
    labels: periodData.map(p => p.label),
    datasets: [{
      label: category,
      data: periodData.map(p => {
        return p.transactions
          .filter(t => t.category === category)
          .reduce((sum, t) => sum + t.amount, 0);
      }),
      borderColor: '#667eea',
      backgroundColor: config.type === 'bar' ? '#667eea' : 'rgba(102, 126, 234, 0.2)',
      tension: 0.4
    }]
  };
};

/**
 * Genera i dati del grafico in base al tipo specificato nella configurazione
 * @param {Object} config - Configurazione del grafico personalizzato
 * @param {Array} transactions - Array di tutte le transazioni
 * @param {Array} accounts - Array di tutti i conti
 * @returns {Object} - Dati formattati per Chart.js
 */
export const getChartData = (config, transactions, accounts) => {
  // Ottiene i dati per il periodo specificato
  const periodData = getPeriodData(config.period, config.options, transactions);
  
  // Genera i dati in base al tipo di visualizzazione
  switch (config.dataType) {
    case 'overview':
      return getOverviewData(periodData, config);
    case 'categories':
      return getCategoriesData(periodData, config);
    case 'accounts':
      return getAccountsData(periodData, config, accounts);
    case 'categoryDetail':
      return getCategoryDetailData(periodData, config);
    default:
      return getOverviewData(periodData, config);
  }
};
