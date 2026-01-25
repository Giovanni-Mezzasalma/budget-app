/**
 * APP.JSX - Core application component
 * Manages all global state and coordinates the various components
 */

import React, { useState, useEffect } from 'react';
import './App.css';

// Import custom hooks
import useLocalStorage from './hooks/useLocalStorage';

// Import default data
import { defaultCategories, defaultAccounts } from './utils/defaultData';

// Import components
import Header from './components/Header/Header';
import Dashboard from './components/Views/Dashboard';
import AccountsView from './components/Views/AccountsView';
import TransactionsView from './components/Views/TransactionsView';
import CategoriesView from './components/Views/CategoriesView';
import CustomChartsView from './components/Views/CustomChartsView';
import AnalysisView from './components/Views/AnalysisView';

// Import modals
import TransactionModal from './components/Modals/TransactionModal';
import TransferModal from './components/Modals/TransferModal';
import AccountModal from './components/Modals/AccountModal';
import CategoryModal from './components/Modals/CategoryModal';
import ChartConfigModal from './components/Modals/ChartConfigModal';

function App() {
  // ===== APPLICATION STATUS =====
  
  // Main data (persistent in localStorage)
  const [accounts, setAccounts] = useLocalStorage('accounts', defaultAccounts);
  const [transactions, setTransactions] = useLocalStorage('transactions', []);
  const [categories, setCategories] = useLocalStorage('categories', JSON.parse(JSON.stringify(defaultCategories)));
  const [savedCharts, setSavedCharts] = useLocalStorage('customCharts', []);
  
  // UI State (non-persistent)
  const [selectedMonth, setSelectedMonth] = useState(new Date().getMonth());
  const [selectedYear, setSelectedYear] = useState(new Date().getFullYear());
  const [activeTab, setActiveTab] = useState('dashboard');
  
  // Modal status (open/closed)
  const [modals, setModals] = useState({
    transaction: false,
    transfer: false,
    account: false,
    category: false,
    chartConfig: false
  });
  
  // Status for the graph in editing (null if new graph)
  const [editingChart, setEditingChart] = useState(null);

  // ===== MODAL MANAGEMENT =====
  
  /**
   * Opens a specific modal
   */
  const openModal = (modalName) => {
    setModals(prev => ({ ...prev, [modalName]: true }));
  };
  
  /**
   * Closes a specific modal
   */
  const closeModal = (modalName) => {
    setModals(prev => ({ ...prev, [modalName]: false }));
    // If we close the chart modal, it resets the editing
    if (modalName === 'chartConfig') {
      setEditingChart(null);
    }
  };

  // ===== ACCOUNT MANAGEMENT =====
  
  /**
   * Add a new account
   */
  const addAccount = (accountData) => {
    const newAccount = {
      ...accountData,
      id: Date.now() // Use timestamp as unique ID
    };
    setAccounts([...accounts, newAccount]);
  };
  
  /**
   * Delete an account and all its transactions
   */
  const deleteAccount = (accountId) => {
    if (window.confirm('Sei sicuro? Questo eliminerà anche tutte le transazioni associate.')) {
      // Remove the account
      setAccounts(accounts.filter(a => a.id !== accountId));
      
      // Removes all associated transactions
      setTransactions(transactions.filter(t => {
        if (t.type === 'transfer') {
          return t.fromAccount !== accountId && t.toAccount !== accountId;
        }
        return t.account !== accountId;
      }));
    }
  };

  // ===== TRANSACTION MANAGEMENT =====
  
  /**
   * Add a new transaction
   */
  const addTransaction = (transactionData) => {
    const newTransaction = {
      ...transactionData,
      id: Date.now() // Use timestamp as unique ID
    };
    setTransactions([...transactions, newTransaction]);
    closeModal('transaction');
  };
  
  /**
   * Add a new transfer
   */
  const addTransfer = (transferData) => {
    const newTransfer = {
      ...transferData,
      type: 'transfer',
      id: Date.now() // Use timestamp as unique ID
    };
    setTransactions([...transactions, newTransfer]);
    closeModal('transfer');
  };
  
  /**
   * Delete a transaction
   */
  const deleteTransaction = (transactionId) => {
    if (window.confirm('Sei sicuro di voler eliminare questa transazione?')) {
      setTransactions(transactions.filter(t => t.id !== transactionId));
    }
  };

  // ===== CATEGORY MANAGEMENT =====
  
  /**
   * Update categories
   */
  const updateCategories = (newCategories) => {
    setCategories(newCategories);
  };
  
  /**
   * Reset categories to default values
   */
  const resetCategories = () => {
    if (window.confirm('Sei sicuro di voler ripristinare tutte le categorie ai valori di default? Questa azione non può essere annullata.')) {
      setCategories(JSON.parse(JSON.stringify(defaultCategories)));
      alert('Categorie ripristinate!');
    }
  };

  // ===== CUSTOM GRAPHICS MANAGEMENT =====
  
  /**
   * Opens the modal for creating a new chart
   */
  const createNewChart = () => {
    setEditingChart(null);
    openModal('chartConfig');
  };
  
  /**
   * Opens the modal for editing an existing chart
   */
  const editChart = (chartId) => {
    const chart = savedCharts.find(c => c.id === chartId);
    if (chart) {
      setEditingChart(chart);
      openModal('chartConfig');
    }
  };
  
  /**
   * Save a chart (new or modified)
   */
  const saveChart = (chartConfig) => {
    const existingIndex = savedCharts.findIndex(c => c.id === chartConfig.id);
    
    if (existingIndex >= 0) {
      // Edit existing chart
      const updatedCharts = [...savedCharts];
      updatedCharts[existingIndex] = chartConfig;
      setSavedCharts(updatedCharts);
    } else {
      // Add new chart
      setSavedCharts([...savedCharts, chartConfig]);
    }
    
    closeModal('chartConfig');
  };
  
  /**
   * Delete a custom chart
   */
  const deleteChart = (chartId) => {
    if (window.confirm('Sei sicuro di voler eliminare questo grafico?')) {
      setSavedCharts(savedCharts.filter(c => c.id !== chartId));
    }
  };

  // ===== RENDER =====
  
  return (
    <div className="App">
      {/* Header with controls and tabs */}
      <Header
        selectedMonth={selectedMonth}
        selectedYear={selectedYear}
        activeTab={activeTab}
        onMonthChange={setSelectedMonth}
        onYearChange={setSelectedYear}
        onTabChange={setActiveTab}
        onOpenTransactionModal={() => openModal('transaction')}
        onOpenTransferModal={() => openModal('transfer')}
        onOpenAccountModal={() => openModal('account')}
        onOpenCategoryModal={() => openModal('category')}
      />

      {/* Main container with the various views */}
      <div className="main-container">
        {/* Dashboard View */}
        {activeTab === 'dashboard' && (
          <Dashboard
            accounts={accounts}
            transactions={transactions}
            selectedMonth={selectedMonth}
            selectedYear={selectedYear}
          />
        )}

        {/* Accounts View */}
        {activeTab === 'accounts' && (
          <AccountsView
            accounts={accounts}
            transactions={transactions}
          />
        )}

        {/* Transactions View */}
        {activeTab === 'transactions' && (
          <TransactionsView
            accounts={accounts}
            transactions={transactions}
            selectedMonth={selectedMonth}
            selectedYear={selectedYear}
            onDeleteTransaction={deleteTransaction}
          />
        )}

        {/* Categories View */}
        {activeTab === 'categories' && (
          <CategoriesView
            transactions={transactions}
            selectedMonth={selectedMonth}
            selectedYear={selectedYear}
          />
        )}

        {/* Custom Charts View */}
        {activeTab === 'customCharts' && (
          <CustomChartsView
            savedCharts={savedCharts}
            transactions={transactions}
            accounts={accounts}
            onCreateChart={createNewChart}
            onEditChart={editChart}
            onDeleteChart={deleteChart}
          />
        )}

        {/* Analysis View */}
        {activeTab === 'analysis' && (
          <AnalysisView
            transactions={transactions}
            selectedMonth={selectedMonth}
            selectedYear={selectedYear}
          />
        )}
      </div>

      {/* Modals */}
      
      {/* Modal for new transaction */}
      <TransactionModal
        isOpen={modals.transaction}
        onClose={() => closeModal('transaction')}
        onSave={addTransaction}
        accounts={accounts}
        categories={categories}
      />

      {/* Modal for new transfer */}
      <TransferModal
        isOpen={modals.transfer}
        onClose={() => closeModal('transfer')}
        onSave={addTransfer}
        accounts={accounts}
      />

      {/* Account management modal */}
      <AccountModal
        isOpen={modals.account}
        onClose={() => closeModal('account')}
        accounts={accounts}
        transactions={transactions}
        onAddAccount={addAccount}
        onDeleteAccount={deleteAccount}
      />

      {/* Modal for category management */}
      <CategoryModal
        isOpen={modals.category}
        onClose={() => closeModal('category')}
        categories={categories}
        onUpdateCategories={updateCategories}
        onResetCategories={resetCategories}
      />

      {/* Modal for graphic configuration */}
      <ChartConfigModal
        isOpen={modals.chartConfig}
        onClose={() => closeModal('chartConfig')}
        onSave={saveChart}
        accounts={accounts}
        categories={categories}
        editingChart={editingChart}
      />
    </div>
  );
}

export default App;
