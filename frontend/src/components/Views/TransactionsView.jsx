/**
 * TRANSACTIONS VIEW COMPONENT
 * Vista che mostra tutte le transazioni in formato tabella
 * con possibilità di eliminarle
 */

import React from 'react';
import { filterTransactionsByMonth, sortTransactionsByDate } from '../../utils/calculations';
import { transactionTypeLabels } from '../../utils/defaultData';

function TransactionsView({ accounts, transactions, selectedMonth, selectedYear, onDeleteTransaction }) {
  // Filtra le transazioni per il mese selezionato
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Ordina le transazioni per data (dalla più recente)
  const sortedTransactions = sortTransactionsByDate(filteredTransactions);

  /**
   * Ottiene la classe CSS per il badge in base al tipo di transazione
   */
  const getBadgeClass = (type) => {
    if (type === 'transfer') return 'badge-transfer';
    if (type === 'income') return 'badge-income';
    if (type === 'expense-necessity') return 'badge-necessity';
    if (type === 'expense-extra') return 'badge-extra';
    return 'badge-withdrawal';
  };

  /**
   * Ottiene l'etichetta del tipo di transazione
   */
  const getTypeLabel = (transaction) => {
    if (transaction.type === 'transfer') {
      return transaction.operationType;
    }
    return transactionTypeLabels[transaction.type];
  };

  /**
   * Ottiene il dettaglio della transazione (categoria e descrizione)
   */
  const getTransactionDetail = (transaction) => {
    if (transaction.type === 'transfer') {
      return transaction.description || '-';
    }
    return `${transaction.category}${transaction.description ? ' - ' + transaction.description : ''}`;
  };

  /**
   * Ottiene le informazioni sul conto/conti coinvolti
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

  // Se non ci sono transazioni, mostra messaggio vuoto
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
              {/* Data */}
              <td>{new Date(t.date).toLocaleDateString('it-IT')}</td>
              
              {/* Tipo con badge colorato */}
              <td>
                <span className={`badge ${getBadgeClass(t.type)}`}>
                  {getTypeLabel(t)}
                </span>
              </td>
              
              {/* Dettaglio (categoria/descrizione) */}
              <td>{getTransactionDetail(t)}</td>
              
              {/* Informazioni conto */}
              <td>{getAccountInfo(t)}</td>
              
              {/* Importo con colore e segno */}
              <td 
                className="text-right" 
                style={{ 
                  fontWeight: 'bold', 
                  color: t.type === 'income' ? '#10b981' : '#ef4444' 
                }}
              >
                {t.type === 'income' ? '+' : '-'}€{t.amount.toFixed(2)}
              </td>
              
              {/* Pulsante elimina */}
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
