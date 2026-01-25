/**
 * CHART CONFIG MODAL COMPONENT
 * Modal for configuring custom charts:
 * - Set the title, chart type, and time period
 * - Select which data to display
 * - Configure specific options for each data type
 */

import React, { useState, useEffect } from 'react';

function ChartConfigModal({ isOpen, onClose, onSave, accounts, categories, editingChart }) {
  // Form Status
  const [formData, setFormData] = useState({
    title: '',
    type: 'line',
    period: 'last6',
    dataType: 'overview',
    options: {
      // Overview Options
      showIncome: true,
      showExpenses: true,
      showNet: true,
      showNecessity: false,
      showExtra: false,
      // Custom period options
      startDate: '',
      endDate: '',
      // Account Options
      selectedAccounts: [],
      // Options for categoryDetail
      category: ''
    }
  });

  // Stato to control the display of the sections
  const [showCustomPeriod, setShowCustomPeriod] = useState(false);
  const [showOverviewOptions, setShowOverviewOptions] = useState(true);
  const [showAccountOptions, setShowAccountOptions] = useState(false);
  const [showCategoryInput, setShowCategoryInput] = useState(false);

  /**
   * Loads chart data into editing when the modal opens
   */
  useEffect(() => {
    if (editingChart) {
      setFormData({
        title: editingChart.title,
        type: editingChart.type,
        period: editingChart.period,
        dataType: editingChart.dataType,
        options: {
          showIncome: editingChart.options.showIncome !== false,
          showExpenses: editingChart.options.showExpenses !== false,
          showNet: editingChart.options.showNet !== false,
          showNecessity: editingChart.options.showNecessity || false,
          showExtra: editingChart.options.showExtra || false,
          startDate: editingChart.options.startDate || '',
          endDate: editingChart.options.endDate || '',
          selectedAccounts: editingChart.options.selectedAccounts || accounts.map(a => a.id),
          category: editingChart.options.category || ''
        }
      });
      
      // Set the section display
      setShowCustomPeriod(editingChart.period === 'custom');
      setShowOverviewOptions(editingChart.dataType === 'overview');
      setShowAccountOptions(editingChart.dataType === 'accounts');
      setShowCategoryInput(editingChart.dataType === 'categoryDetail');
    } else {
      // Reset for new chart
      setFormData({
        title: '',
        type: 'line',
        period: 'last6',
        dataType: 'overview',
        options: {
          showIncome: true,
          showExpenses: true,
          showNet: true,
          showNecessity: false,
          showExtra: false,
          startDate: '',
          endDate: '',
          selectedAccounts: accounts.map(a => a.id),
          category: ''
        }
      });
      
      setShowCustomPeriod(false);
      setShowOverviewOptions(true);
      setShowAccountOptions(false);
      setShowCategoryInput(false);
    }
  }, [editingChart, accounts, isOpen]);

  /**
   * Manages changes in basic form fields
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));

    // Manages custom period display
    if (name === 'period') {
      setShowCustomPeriod(value === 'custom');
    }

    // Manages the display of data options
    if (name === 'dataType') {
      setShowOverviewOptions(value === 'overview');
      setShowAccountOptions(value === 'accounts');
      setShowCategoryInput(value === 'categoryDetail');
    }
  };

  /**
   * Handles changes in options (checkboxes, selects, etc.)
   */
  const handleOptionChange = (optionName, value) => {
    setFormData(prev => ({
      ...prev,
      options: { ...prev.options, [optionName]: value }
    }));
  };

  /**
   * Manages checkbox toggles for accounts
   */
  const handleAccountToggle = (accountId) => {
    setFormData(prev => {
      const currentAccounts = prev.options.selectedAccounts || [];
      const isSelected = currentAccounts.includes(accountId);
      
      const newAccounts = isSelected
        ? currentAccounts.filter(id => id !== accountId)
        : [...currentAccounts, accountId];
      
      return {
        ...prev,
        options: { ...prev.options, selectedAccounts: newAccounts }
      };
    });
  };

  /**
   * Gets all categories available for selection
   */
  const getAllCategories = () => {
    const allCats = [];
    
    Object.values(categories).forEach(catGroup => {
      if (Array.isArray(catGroup)) {
        allCats.push(...catGroup);
      } else {
        Object.values(catGroup).forEach(subcats => {
          allCats.push(...subcats);
        });
      }
    });
    
    return allCats;
  };

  /**
   * Manages form submission
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Create chart configuration
    const config = {
      id: editingChart ? editingChart.id : Date.now(),
      title: formData.title,
      type: formData.type,
      period: formData.period,
      dataType: formData.dataType,
      options: { ...formData.options }
    };
    
    // Call the save function
    onSave(config);
  };

  // If the modal is not open, it does not render anything
  if (!isOpen) return null;

  const allCategories = getAllCategories();

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{editingChart ? 'Modifica Grafico' : 'Nuovo Grafico Personalizzato'}</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        <form onSubmit={handleSubmit}>
          {/* Graphic Title */}
          <div className="form-group">
            <label>Titolo Grafico</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              placeholder="Es: Andamento Entrate 2025"
              required
            />
          </div>

          {/* Type, Period and Data Type */}
          <div className="form-row-3">
            <div className="form-group">
              <label>Tipo Grafico</label>
              <select name="type" value={formData.type} onChange={handleChange} required>
                <option value="line">Linee</option>
                <option value="bar">Barre</option>
                <option value="pie">Torta</option>
                <option value="doughnut">Ciambella</option>
              </select>
            </div>

            <div className="form-group">
              <label>Periodo</label>
              <select name="period" value={formData.period} onChange={handleChange} required>
                <option value="last3">Ultimi 3 Mesi</option>
                <option value="last6">Ultimi 6 Mesi</option>
                <option value="last12">Ultimi 12 Mesi</option>
                <option value="currentYear">Anno Corrente</option>
                <option value="custom">Periodo Personalizzato</option>
              </select>
            </div>

            <div className="form-group">
              <label>Visualizza Dati</label>
              <select name="dataType" value={formData.dataType} onChange={handleChange} required>
                <option value="overview">Panoramica (Entrate/Uscite/Netto)</option>
                <option value="categories">Per Categoria</option>
                <option value="accounts">Per Conto</option>
                <option value="categoryDetail">Dettaglio Categoria Specifica</option>
              </select>
            </div>
          </div>

          {/* Custom Period */}
          {showCustomPeriod && (
            <div className="form-row">
              <div className="form-group">
                <label>Data Inizio</label>
                <input
                  type="month"
                  value={formData.options.startDate}
                  onChange={(e) => handleOptionChange('startDate', e.target.value)}
                />
              </div>
              <div className="form-group">
                <label>Data Fine</label>
                <input
                  type="month"
                  value={formData.options.endDate}
                  onChange={(e) => handleOptionChange('endDate', e.target.value)}
                />
              </div>
            </div>
          )}

          {/* Specific Category Options */}
          {showCategoryInput && (
            <div className="form-group">
              <label>Seleziona Categoria</label>
              <select
                value={formData.options.category}
                onChange={(e) => handleOptionChange('category', e.target.value)}
              >
                <option value="">Seleziona categoria</option>
                {allCategories.map((cat, index) => (
                  <option key={index} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>
          )}

          {/* Options Overview */}
          {showOverviewOptions && (
            <div className="form-group">
              <label>Dati da Mostrare</label>
              <div className="checkbox-group">
                <div className="checkbox-item">
                  <input
                    type="checkbox"
                    id="showIncome"
                    checked={formData.options.showIncome}
                    onChange={(e) => handleOptionChange('showIncome', e.target.checked)}
                  />
                  <label htmlFor="showIncome">Entrate</label>
                </div>
                <div className="checkbox-item">
                  <input
                    type="checkbox"
                    id="showExpenses"
                    checked={formData.options.showExpenses}
                    onChange={(e) => handleOptionChange('showExpenses', e.target.checked)}
                  />
                  <label htmlFor="showExpenses">Uscite</label>
                </div>
                <div className="checkbox-item">
                  <input
                    type="checkbox"
                    id="showNet"
                    checked={formData.options.showNet}
                    onChange={(e) => handleOptionChange('showNet', e.target.checked)}
                  />
                  <label htmlFor="showNet">Netto</label>
                </div>
                <div className="checkbox-item">
                  <input
                    type="checkbox"
                    id="showNecessity"
                    checked={formData.options.showNecessity}
                    onChange={(e) => handleOptionChange('showNecessity', e.target.checked)}
                  />
                  <label htmlFor="showNecessity">Solo Necessità</label>
                </div>
                <div className="checkbox-item">
                  <input
                    type="checkbox"
                    id="showExtra"
                    checked={formData.options.showExtra}
                    onChange={(e) => handleOptionChange('showExtra', e.target.checked)}
                  />
                  <label htmlFor="showExtra">Solo Extra</label>
                </div>
              </div>
            </div>
          )}

          {/* Account Options */}
          {showAccountOptions && (
            <div className="form-group">
              <label>Conti da Includere</label>
              <div className="checkbox-group">
                {accounts.map((acc) => (
                  <div key={acc.id} className="checkbox-item">
                    <input
                      type="checkbox"
                      id={`acc-${acc.id}`}
                      checked={formData.options.selectedAccounts?.includes(acc.id)}
                      onChange={() => handleAccountToggle(acc.id)}
                    />
                    <label htmlFor={`acc-${acc.id}`}>{acc.name}</label>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Buttons */}
          <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
            <button type="submit" className="btn btn-primary" style={{ flex: 1 }}>
              Salva Grafico
            </button>
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Annulla
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default ChartConfigModal;
