/**
 * DASHBOARD COMPONENT
 * Main dashboard view showing:
 * - Total Assets
 * - Monthly Income
 * - Monthly Expenses
 * - Monthly Net Income
 */

import React from 'react';
import { calculateTotalBalance, calculateStats, filterTransactionsByMonth } from '../../utils/calculations';

function Dashboard({ accounts, transactions, selectedMonth, selectedYear }) {
  // Filter transactions for the selected month
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Calculate statistics for the month
  const stats = calculateStats(filteredTransactions);
  
  // Calculate total assets
  const totalBalance = calculateTotalBalance(accounts, transactions);

  return (
    <div className="kpi-grid">
      {/* KPI: Total Assets */}
      <div className="kpi-card income">
        <div className="kpi-label">Patrimonio Totale</div>
        <div className="kpi-value">€{totalBalance.toFixed(2)}</div>
      </div>

      {/* KPI: Revenue */}
      <div className="kpi-card income">
        <div className="kpi-label">Entrate</div>
        <div className="kpi-value">€{stats.income.toFixed(2)}</div>
      </div>

      {/* KPI: Total Expenses */}
      <div className="kpi-card expense">
        <div className="kpi-label">Uscite Totali</div>
        <div className="kpi-value">€{stats.totalExpenses.toFixed(2)}</div>
      </div>

      {/* KPI: Monthly Net */}
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
