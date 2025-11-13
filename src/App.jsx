/**
 * APP.JSX - Componente principale dell'applicazione
 * Gestisce tutto lo stato globale e coordina i vari componenti
 */

import React, { useState, useEffect } from 'react';
import './App.css';

// Import degli hooks personalizzati
import useLocalStorage from './hooks/useLocalStorage';

// Import dei dati di default
import { defaultCategories, defaultAccounts } from './utils/defaultData';

// Import dei componenti
import Header from './components/Header/Header';
import Dashboard from './components/Views/Dashboard';
import AccountsView from './components/Views/AccountsView';
import TransactionsView from './components/Views/TransactionsView';
import CategoriesView from './components/Views/CategoriesView';
import CustomChartsView from './components/Views/CustomChartsView';
import AnalysisView from './components/Views/AnalysisView';

// Import dei modali
import TransactionModal from './components/Modals/TransactionModal';
import TransferModal from './components/Modals/TransferModal';
import AccountModal from './components/Modals/AccountModal';
import CategoryModal from './components/Modals/CategoryModal';
import ChartConfigModal from './components/Modals/ChartConfigModal';

function App() {
  // ===== STATO DELL'APPLICAZIONE =====
  
  // Dati principali (persistenti in localStorage)
  const [accounts, setAccounts] = useLocalStorage('accounts', defaultAccounts);
  const [transactions, setTransactions] = useLocalStorage('transactions', []);
  const [categories, setCategories] = useLocalStorage('categories', JSON.parse(JSON.stringify(defaultCategories)));
  const [savedCharts, setSavedCharts] = useLocalStorage('customCharts', []);
  
  // Stato della UI (non persistente)
  const [selectedMonth, setSelectedMonth] = useState(new Date().getMonth());
  const [selectedYear, setSelectedYear] = useState(new Date().getFullYear());
  const [activeTab, setActiveTab] = useState('dashboard');
  
  // Stato dei modali (aperti/chiusi)
  const [modals, setModals] = useState({
    transaction: false,
    transfer: false,
    account: false,
    category: false,
    chartConfig: false
  });
  
  // Stato per il grafico in editing (null se nuovo grafico)
  const [editingChart, setEditingChart] = useState(null);

  // ===== GESTIONE MODALI =====
  
  /**
   * Apre un modal specifico
   */
  const openModal = (modalName) => {
    setModals(prev => ({ ...prev, [modalName]: true }));
  };
  
  /**
   * Chiude un modal specifico
   */
  const closeModal = (modalName) => {
    setModals(prev => ({ ...prev, [modalName]: false }));
    // Se chiudiamo il modal del grafico, resetta l'editing
    if (modalName === 'chartConfig') {
      setEditingChart(null);
    }
  };

  // ===== GESTIONE CONTI =====
  
  /**
   * Aggiunge un nuovo conto
   */
  const addAccount = (accountData) => {
    const newAccount = {
      ...accountData,
      id: Date.now() // Usa timestamp come ID univoco
    };
    setAccounts([...accounts, newAccount]);
  };
  
  /**
   * Elimina un conto e tutte le sue transazioni
   */
  const deleteAccount = (accountId) => {
    if (window.confirm('Sei sicuro? Questo eliminerà anche tutte le transazioni associate.')) {
      // Rimuove il conto
      setAccounts(accounts.filter(a => a.id !== accountId));
      
      // Rimuove tutte le transazioni associate
      setTransactions(transactions.filter(t => {
        if (t.type === 'transfer') {
          return t.fromAccount !== accountId && t.toAccount !== accountId;
        }
        return t.account !== accountId;
      }));
    }
  };

  // ===== GESTIONE TRANSAZIONI =====
  
  /**
   * Aggiunge una nuova transazione
   */
  const addTransaction = (transactionData) => {
    const newTransaction = {
      ...transactionData,
      id: Date.now() // Usa timestamp come ID univoco
    };
    setTransactions([...transactions, newTransaction]);
    closeModal('transaction');
  };
  
  /**
   * Aggiunge un nuovo trasferimento
   */
  const addTransfer = (transferData) => {
    const newTransfer = {
      ...transferData,
      type: 'transfer',
      id: Date.now() // Usa timestamp come ID univoco
    };
    setTransactions([...transactions, newTransfer]);
    closeModal('transfer');
  };
  
  /**
   * Elimina una transazione
   */
  const deleteTransaction = (transactionId) => {
    if (window.confirm('Sei sicuro di voler eliminare questa transazione?')) {
      setTransactions(transactions.filter(t => t.id !== transactionId));
    }
  };

  // ===== GESTIONE CATEGORIE =====
  
  /**
   * Aggiorna le categorie
   */
  const updateCategories = (newCategories) => {
    setCategories(newCategories);
  };
  
  /**
   * Ripristina le categorie ai valori di default
   */
  const resetCategories = () => {
    if (window.confirm('Sei sicuro di voler ripristinare tutte le categorie ai valori di default? Questa azione non può essere annullata.')) {
      setCategories(JSON.parse(JSON.stringify(defaultCategories)));
      alert('Categorie ripristinate!');
    }
  };

  // ===== GESTIONE GRAFICI PERSONALIZZATI =====
  
  /**
   * Apre il modal per creare un nuovo grafico
   */
  const createNewChart = () => {
    setEditingChart(null);
    openModal('chartConfig');
  };
  
  /**
   * Apre il modal per modificare un grafico esistente
   */
  const editChart = (chartId) => {
    const chart = savedCharts.find(c => c.id === chartId);
    if (chart) {
      setEditingChart(chart);
      openModal('chartConfig');
    }
  };
  
  /**
   * Salva un grafico (nuovo o modificato)
   */
  const saveChart = (chartConfig) => {
    const existingIndex = savedCharts.findIndex(c => c.id === chartConfig.id);
    
    if (existingIndex >= 0) {
      // Modifica grafico esistente
      const updatedCharts = [...savedCharts];
      updatedCharts[existingIndex] = chartConfig;
      setSavedCharts(updatedCharts);
    } else {
      // Aggiungi nuovo grafico
      setSavedCharts([...savedCharts, chartConfig]);
    }
    
    closeModal('chartConfig');
  };
  
  /**
   * Elimina un grafico personalizzato
   */
  const deleteChart = (chartId) => {
    if (window.confirm('Sei sicuro di voler eliminare questo grafico?')) {
      setSavedCharts(savedCharts.filter(c => c.id !== chartId));
    }
  };

  // ===== RENDER =====
  
  return (
    <div className="App">
      {/* Header con controlli e tabs */}
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

      {/* Container principale con le varie viste */}
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

      {/* Modali */}
      
      {/* Modal per nuova transazione */}
      <TransactionModal
        isOpen={modals.transaction}
        onClose={() => closeModal('transaction')}
        onSave={addTransaction}
        accounts={accounts}
        categories={categories}
      />

      {/* Modal per nuovo trasferimento */}
      <TransferModal
        isOpen={modals.transfer}
        onClose={() => closeModal('transfer')}
        onSave={addTransfer}
        accounts={accounts}
      />

      {/* Modal per gestione conti */}
      <AccountModal
        isOpen={modals.account}
        onClose={() => closeModal('account')}
        accounts={accounts}
        transactions={transactions}
        onAddAccount={addAccount}
        onDeleteAccount={deleteAccount}
      />

      {/* Modal per gestione categorie */}
      <CategoryModal
        isOpen={modals.category}
        onClose={() => closeModal('category')}
        categories={categories}
        onUpdateCategories={updateCategories}
        onResetCategories={resetCategories}
      />

      {/* Modal per configurazione grafico */}
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
