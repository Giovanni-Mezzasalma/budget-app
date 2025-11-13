/**
 * ANALYSIS VIEW COMPONENT
 * Vista per l'analisi avanzata con:
 * - Grafico andamento ultimi 6 mesi
 * - Grafico a torta delle spese mensili
 * - Grafico a barre per categoria
 * - Statistiche e medie
 * - Tabella di confronto mensile
 */

import React from 'react';
import TrendChart from '../Charts/TrendChart';
import PieChart from '../Charts/PieChart';
import CategoryChart from '../Charts/CategoryChart';
import { getLastMonthsData, calculateStats, filterTransactionsByMonth } from '../../utils/calculations';

function AnalysisView({ transactions, selectedMonth, selectedYear }) {
  // Ottiene i dati degli ultimi 6 mesi
  const last6MonthsData = getLastMonthsData(6, selectedMonth, selectedYear, transactions);
  
  // Calcola le statistiche per il mese corrente
  const currentMonthTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  const currentStats = calculateStats(currentMonthTransactions);

  // Calcola le medie degli ultimi 6 mesi
  const avgIncome = last6MonthsData.reduce((sum, m) => sum + m.income, 0) / last6MonthsData.length;
  const avgExpenses = last6MonthsData.reduce((sum, m) => sum + m.expenses, 0) / last6MonthsData.length;
  const avgNet = last6MonthsData.reduce((sum, m) => sum + m.net, 0) / last6MonthsData.length;
  
  // Calcola il tasso di risparmio
  const savingsRate = currentStats.income > 0 ? ((currentStats.net / currentStats.income) * 100) : 0;

  return (
    <div className="card">
      <h2>📊 Analisi Standard</h2>

      {/* Grafico andamento ultimi 6 mesi */}
      <h3>Andamento Ultimi 6 Mesi</h3>
      <TrendChart data={last6MonthsData} />

      {/* Grafico a torta spese mensili */}
      <h3>Distribuzione Spese Mensili</h3>
      <PieChart transactions={currentMonthTransactions} />

      {/* Grafico a barre per categoria */}
      <h3>Confronto per Categoria (Top 10)</h3>
      <CategoryChart transactions={currentMonthTransactions} />

      {/* Statistiche e medie */}
      <h3>Statistiche e Medie</h3>
      <div className="stats-grid">
        <div className="stat-box">
          <div className="label">Media Entrate (6 mesi)</div>
          <div className="value">€{avgIncome.toFixed(2)}</div>
        </div>
        <div className="stat-box">
          <div className="label">Media Uscite (6 mesi)</div>
          <div className="value">€{avgExpenses.toFixed(2)}</div>
        </div>
        <div className="stat-box">
          <div className="label">Media Netto (6 mesi)</div>
          <div className="value">€{avgNet.toFixed(2)}</div>
        </div>
        <div className="stat-box">
          <div className="label">Tasso Risparmio</div>
          <div className="value">{savingsRate.toFixed(1)}%</div>
        </div>
      </div>

      {/* Tabella di confronto mensile */}
      <h3>Confronto Mensile</h3>
      <div className="comparison-table">
        <table>
          <thead>
            <tr>
              <th>Mese</th>
              <th className="text-right">Entrate</th>
              <th className="text-right">Uscite</th>
              <th className="text-right">Netto</th>
              <th className="text-center">Var. vs Precedente</th>
            </tr>
          </thead>
          <tbody>
            {last6MonthsData.map((m, i) => {
              // Calcola la variazione rispetto al mese precedente
              let variation = '';
              if (i > 0) {
                const diff = m.net - last6MonthsData[i - 1].net;
                const percent = last6MonthsData[i - 1].net !== 0 
                  ? ((diff / Math.abs(last6MonthsData[i - 1].net)) * 100) 
                  : 0;
                variation = (
                  <span className={diff >= 0 ? 'trend-up' : 'trend-down'}>
                    {diff >= 0 ? '▲' : '▼'} €{Math.abs(diff).toFixed(2)} ({percent.toFixed(1)}%)
                  </span>
                );
              }

              return (
                <tr key={i}>
                  <td><strong>{m.label}</strong></td>
                  <td className="text-right">€{m.income.toFixed(2)}</td>
                  <td className="text-right">€{m.expenses.toFixed(2)}</td>
                  <td 
                    className="text-right" 
                    style={{ 
                      color: m.net >= 0 ? '#10b981' : '#ef4444', 
                      fontWeight: 'bold' 
                    }}
                  >
                    €{m.net.toFixed(2)}
                  </td>
                  <td className="text-center">{variation || '-'}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AnalysisView;
