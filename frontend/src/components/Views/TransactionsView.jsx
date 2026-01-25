/**
 * TRANSACTIONS VIEW COMPONENT
 * View showing all transactions in table format
 * with the ability to delete them
 */

import React from 'react';
import { filterTransactionsByMonth, sortTransactionsByDate } from '../../utils/calculations';
import { transactionTypeLabels } from '../../utils/defaultData';

function TransactionsView({ accounts, transactions, selectedMonth, selectedYear, onDeleteTransaction }) {
  // Filter transactions for the selected month
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Sort transactions by date (most recent first)
  const sortedTransactions = sortTransactionsByDate(filteredTransactions);

  /**
   * Gets the CSS class for the badge based on the transaction type
   */
  const getBadgeClass = (type) => {
    if (type === 'transfer') return 'badge-transfer';
    if (type === 'income') return 'badge-income';
    if (type === 'expense-necessity') return 'badge-necessity';
    if (type === 'expense-extra') return 'badge-extra';
    return 'badge-withdrawal';
  };

  /**
   * Gets the transaction type label
   */
  const getTypeLabel = (transaction) => {
    if (transaction.type === 'transfer') {
      return transaction.operationType;
    }
    return transactionTypeLabels[transaction.type];
  };

  /**
   * Gets the transaction details (category and description)
   */
  const getTransactionDetail = (transaction) => {
    if (transaction.type === 'transfer') {
      return transaction.description || '-';
    }
    return `${transaction.category}${transaction.description ? ' - ' + transaction.description : ''}`;
  };

  /**
   * Gets information about the account(s) involved
   */
  const getAccountInfo = (transaction) => {
    if (transaction.type === 'transfer') {
      const fromAcc = accounts.find(a => a.id === transaction.fromAccount);
      const toAcc = accounts.find(a => a.id === transaction.toAccount);
      return `${fromAcc?.name || '-'} → ${toAcc?.name || '-'}`;
    }
    const acc = accounts.find(a => a.id === transaction.account);
    return acc?.name || '-';
  };

  // If there are no transactions, show blank message
  if (sortedTransactions.length === 0) {
    return (
      <div className="card">
        <h2>Tutte le Transazioni</h2>
        <div className="empty-state">
          <h3>Nessuna transazione</h3>
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Tutte le Transazioni</h2>
      <table>
        <thead>
          <tr>
            <th>Data</th>
            <th>Tipo</th>
            <th>Dettaglio</th>
            <th>Conto</th>
            <th className="text-right">Importo</th>
            <th className="text-center">Azioni</th>
          </tr>
        </thead>
        <tbody>
          {sortedTransactions.map((t) => (
            <tr key={t.id}>
              {/* Date */}
              <td>{new Date(t.date).toLocaleDateString('it-IT')}</td>
              
              {/* Type with colored badge */}
              <td>
                <span className={`badge ${getBadgeClass(t.type)}`}>
                  {getTypeLabel(t)}
                </span>
              </td>
              
              {/* Detail (category/description) */}
              <td>{getTransactionDetail(t)}</td>
              
              {/* Account Information */}
              <td>{getAccountInfo(t)}</td>
              
              {/* Amount with color and sign */}
              <td 
                className="text-right" 
                style={{ 
                  fontWeight: 'bold', 
                  color: t.type === 'income' ? '#10b981' : '#ef4444' 
                }}
              >
                {t.type === 'income' ? '+' : '-'}€{t.amount.toFixed(2)}
              </td>
              
              {/* Delete button */}
              <td className="text-center">
                <button 
                  className="btn-danger" 
                  onClick={() => onDeleteTransaction(t.id)}
                >
                  Elimina
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TransactionsView;
