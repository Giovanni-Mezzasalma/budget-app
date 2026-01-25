/**
 * HEADER COMPONENT
 * Header component containing:
 * - Application title
 * - Quick action buttons
 * - Month and year selectors
 * - Navigation tabs
 */

import React from 'react';
import './Header.css';

function Header({
  selectedMonth,
  selectedYear,
  activeTab,
  onMonthChange,
  onYearChange,
  onTabChange,
  onOpenTransactionModal,
  onOpenTransferModal,
  onOpenAccountModal,
  onOpenCategoryModal
}) {
  // Array of months for the selector
  const months = [
    'Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
    'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'
  ];

  // Array of available years
  const years = [2023, 2024, 2025, 2026];

  // Array of tabs with icons and IDs
  const tabs = [
    { id: 'dashboard', label: '📊 Dashboard' },
    { id: 'accounts', label: '🏦 Conti' },
    { id: 'transactions', label: '📝 Transazioni' },
    { id: 'categories', label: '📂 Categorie' },
    { id: 'customCharts', label: '📈 Grafici Personalizzati' },
    { id: 'analysis', label: '📊 Analisi' }
  ];

  return (
    <div className="header">
      {/* Main Title */}
      <h1>💰 Gestione Bilancio Completa</h1>

      {/* Quick action buttons */}
      <div className="quick-actions">
        <button className="btn btn-primary" onClick={onOpenTransactionModal}>
          💵 Entrata/Spesa
        </button>
        <button className="btn btn-success" onClick={onOpenTransferModal}>
          🔄 Trasferimento
        </button>
        <button className="btn btn-info" onClick={onOpenAccountModal}>
          🏦 Gestisci Conti
        </button>
        <button className="btn btn-warning" onClick={onOpenCategoryModal}>
          📂 Gestisci Categorie
        </button>
      </div>

      {/* Checks by month and year */}
      <div className="controls">
        <select 
          value={selectedMonth} 
          onChange={(e) => onMonthChange(parseInt(e.target.value))}
        >
          {months.map((month, index) => (
            <option key={index} value={index}>
              {month}
            </option>
          ))}
        </select>

        <select 
          value={selectedYear} 
          onChange={(e) => onYearChange(parseInt(e.target.value))}
        >
          {years.map((year) => (
            <option key={year} value={year}>
              {year}
            </option>
          ))}
        </select>
      </div>

      {/* Navigation tabs */}
      <div className="tabs">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            className={`tab ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => onTabChange(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export default Header;
