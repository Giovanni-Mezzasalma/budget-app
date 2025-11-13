/**
 * TRANSACTION MODAL COMPONENT
 * Modal per aggiungere una nuova transazione (entrata o spesa)
 */

import React, { useState, useEffect } from 'react';

function TransactionModal({ isOpen, onClose, onSave, accounts, categories }) {
  // Stato del form
  const [formData, setFormData] = useState({
    date: new Date().toISOString().split('T')[0],
    type: 'expense-necessity',
    category: '',
    account: '',
    amount: '',
    description: ''
  });

  // Array delle categorie disponibili per il tipo selezionato
  const [availableCategories, setAvailableCategories] = useState([]);

  /**
   * Aggiorna le categorie disponibili quando cambia il tipo di transazione
   */
  useEffect(() => {
    const cats = categories[formData.type];
    
    if (Array.isArray(cats)) {
      // Categorie semplici (array)
      setAvailableCategories(cats.map(cat => ({ value: cat, label: cat, group: null })));
    } else {
      // Categorie con gruppi (oggetto)
      const categoriesWithGroups = [];
      Object.keys(cats).forEach(group => {
        cats[group].forEach(cat => {
          categoriesWithGroups.push({ value: cat, label: cat, group: group });
        });
      });
      setAvailableCategories(categoriesWithGroups);
    }
    
    // Reset della categoria quando cambia il tipo
    setFormData(prev => ({ ...prev, category: '' }));
  }, [formData.type, categories]);

  /**
   * Gestisce i cambiamenti nei campi del form
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  /**
   * Gestisce il submit del form
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Crea l'oggetto transazione
    const transaction = {
      ...formData,
      account: parseInt(formData.account),
      amount: parseFloat(formData.amount)
    };
    
    // Chiama la funzione di salvataggio
    onSave(transaction);
    
    // Reset del form
    setFormData({
      date: new Date().toISOString().split('T')[0],
      type: 'expense-necessity',
      category: '',
      account: '',
      amount: '',
      description: ''
    });
  };

  // Se il modal non è aperto, non renderizza nulla
  if (!isOpen) return null;

  // Raggruppa le categorie per gruppo se necessario
  const categoryGroups = {};
  availableCategories.forEach(cat => {
    if (cat.group) {
      if (!categoryGroups[cat.group]) categoryGroups[cat.group] = [];
      categoryGroups[cat.group].push(cat);
    }
  });

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Nuova Transazione</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        <form onSubmit={handleSubmit}>
          {/* Data */}
          <div className="form-group">
            <label>Data</label>
            <input
              type="date"
              name="date"
              value={formData.date}
              onChange={handleChange}
              required
            />
          </div>

          {/* Tipo */}
          <div className="form-group">
            <label>Tipo</label>
            <select
              name="type"
              value={formData.type}
              onChange={handleChange}
              required
            >
              <option value="income">Entrata</option>
              <option value="expense-necessity">Spesa di Necessità</option>
              <option value="expense-extra">Spesa Extra</option>
              <option value="withdrawal">Prelievo</option>
            </select>
          </div>

          {/* Categoria e Conto */}
          <div className="form-row">
            <div className="form-group">
              <label>Categoria</label>
              <select
                name="category"
                value={formData.category}
                onChange={handleChange}
                required
              >
                <option value="">Seleziona</option>
                {Object.keys(categoryGroups).length > 0 ? (
                  // Categorie con gruppi
                  Object.keys(categoryGroups).map(group => (
                    <optgroup key={group} label={group}>
                      {categoryGroups[group].map(cat => (
                        <option key={cat.value} value={cat.value}>
                          {cat.label}
                        </option>
                      ))}
                    </optgroup>
                  ))
                ) : (
                  // Categorie semplici
                  availableCategories.map(cat => (
                    <option key={cat.value} value={cat.value}>
                      {cat.label}
                    </option>
                  ))
                )}
              </select>
            </div>

            <div className="form-group">
              <label>Conto</label>
              <select
                name="account"
                value={formData.account}
                onChange={handleChange}
                required
              >
                <option value="">Seleziona</option>
                {accounts.map(acc => (
                  <option key={acc.id} value={acc.id}>
                    {acc.name}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Importo */}
          <div className="form-group">
            <label>Importo (€)</label>
            <input
              type="number"
              name="amount"
              value={formData.amount}
              onChange={handleChange}
              step="0.01"
              min="0"
              required
            />
          </div>

          {/* Descrizione */}
          <div className="form-group">
            <label>Descrizione (opzionale)</label>
            <input
              type="text"
              name="description"
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          {/* Pulsanti */}
          <div style={{ display: 'flex', gap: '10px' }}>
            <button type="submit" className="btn btn-primary" style={{ flex: 1 }}>
              Aggiungi
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

export default TransactionModal;
