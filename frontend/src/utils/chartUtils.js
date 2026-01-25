/**
 * CHART UTILITIES
 * Contains utility functions for generating custom chart data
 */

import { filterTransactionsByMonth } from './calculations';

/**
 * Gets data for a specific period based on your configuration
 * @param {string} period - Period type ('last3', 'last6', 'last12', 'currentYear', 'custom')
 * @param {Object} options - Additional options (startDate, endDate for custom period)
 * @param {Array} transactions - Array of all transactions
 * @returns {Array} - Array of monthly data for the specified period
 */
export const getPeriodData = (period, options, transactions) => {
  const data = [];
  let startDate, endDate, months;

  const currentMonth = new Date().getMonth();
  const currentYear = new Date().getFullYear();

  // Determines the number of months and dates based on the selected period
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
      // Current year: from January to December
      startDate = new Date(currentYear, 0, 1);
      endDate = new Date(currentYear, 11, 31);
      months = 12;
      break;
    case 'custom':
      // Custom period: Use the dates provided in the options
      if (options.startDate && options.endDate) {
        const start = new Date(options.startDate + '-01');
        const end = new Date(options.endDate + '-01');
        months = (end.getFullYear() - start.getFullYear()) * 12 + 
                (end.getMonth() - start.getMonth()) + 1;
        startDate = start;
      } else {
        months = 6; // Default if dates are not provided
      }
      break;
    default:
      months = 6;
  }

  // Generate data for each month of the period
  for (let i = months - 1; i >= 0; i--) {
    const date = startDate ? 
      new Date(startDate.getFullYear(), startDate.getMonth() + (months - 1 - i), 1) :
      new Date(currentYear, currentMonth - i, 1);
    
    const month = date.getMonth();
    const year = date.getFullYear();
    
    // Filter transactions for this month
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
 * Generate data for an overview chart (income/expense/net)
 * @param {Array} periodData - Monthly data for the period
 * @param {Object} config - Chart Setup
 * @returns {Object} - Data formatted for Chart.js
 */
export const getOverviewData = (periodData, config) => {
  const datasets = [];
  
  // Revenue Dataset
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

  // Dataset for total expenditures
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

  // Dataset for essential expenses
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

  // Dataset for extra expenses
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

  // Dataset for the net
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
 * Generate data for a category chart
 * @param {Array} periodData - Monthly data for the period
 * @param {Object} config - Chart Setup
 * @returns {Object} - Data formatted for Chart.js
 */
export const getCategoriesData = (periodData, config) => {
  const categoryTotals = {};
  
  // Add up the expenses per category over the entire period
  periodData.forEach(p => {
    p.transactions.filter(t => t.type !== 'income' && t.type !== 'transfer').forEach(t => {
      categoryTotals[t.category] = (categoryTotals[t.category] || 0) + t.amount;
    });
  });

  // Sort categories by decreasing amount and take the top 10
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
 * Generate data for an accounts chart
 * @param {Array} periodData - Monthly data for the period
 * @param {Object} config - Chart Setup
 * @param {Array} accounts - Array of all accounts
 * @returns {Object} - Data formatted for Chart.js
 */
export const getAccountsData = (periodData, config, accounts) => {
  const selectedAccounts = config.options.selectedAccounts || accounts.map(a => a.id);
  const datasets = [];

  // Colors for different accounts
  const colors = ['#667eea', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899'];

  selectedAccounts.forEach((accId, index) => {
    const account = accounts.find(a => a.id === accId);
    if (!account) return;

    datasets.push({
      label: account.name,
      data: periodData.map(p => {
        let balance = 0;
        // Calculate the monthly balance for this account
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
 * Generate data for a detail chart of a specific category
 * @param {Array} periodData - Monthly data for the period
 * @param {Object} config - Chart Setup
 * @returns {Object} - Data formatted for Chart.js
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
 * Generates chart data based on the type specified in the configuration
 * @param {Object} config - Configuring the custom chart
 * @param {Array} transactions - Array of all transactions
 * @param {Array} accounts - Array of all accounts
 * @returns {Object} - Data formatted for Chart.js
 */
export const getChartData = (config, transactions, accounts) => {
  // Gets data for the specified period
  const periodData = getPeriodData(config.period, config.options, transactions);
  
  // Generate data based on the view type
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
