/**
 * DASHBOARD COMPONENT
 * Vista dashboard principale che mostra:
 * - Patrimonio totale
 * - Entrate mensili
 * - Uscite mensili
 * - Netto mensile
 */

import React from 'react';
import { calculateTotalBalance, calculateStats, filterTransactionsByMonth } from '../../utils/calculations';

function Dashboard({ accounts, transactions, selectedMonth, selectedYear }) {
  // Filtra le transazioni per il mese selezionato
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Calcola le statistiche per il mese
  const stats = calculateStats(filteredTransactions);
  
  // Calcola il patrimonio totale
  const totalBalance = calculateTotalBalance(accounts, transactions);

  return (
    <div className="kpi-grid">
      {/* KPI: Patrimonio Totale */}
      <div className="kpi-card income">
        <div className="kpi-label">Patrimonio Totale</div>
        <div className="kpi-value">€{totalBalance.toFixed(2)}</div>
      </div>

      {/* KPI: Entrate */}
      <div className="kpi-card income">
        <div className="kpi-label">Entrate</div>
        <div className="kpi-value">€{stats.income.toFixed(2)}</div>
      </div>

      {/* KPI: Uscite Totali */}
      <div className="kpi-card expense">
        <div className="kpi-label">Uscite Totali</div>
        <div className="kpi-value">€{stats.totalExpenses.toFixed(2)}</div>
      </div>

      {/* KPI: Netto Mensile */}
      <div className="kpi-card net">
        <div className="kpi-label">Netto Mensile</div>
        <div 
          className="kpi-value" 
          style={{ color: stats.net >= 0 ? '#10b981' : '#ef4444' }}
        >
          €{stats.net.toFixed(2)}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
