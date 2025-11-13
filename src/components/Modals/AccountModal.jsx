/**
 * ACCOUNT MODAL COMPONENT
 * Modal per gestire i conti bancari:
 * - Visualizzare i conti esistenti
 * - Aggiungere nuovi conti
 * - Eliminare conti
 */

import React, { useState } from 'react';
import { calculateAccountBalance } from '../../utils/calculations';
import { accountTypeLabels } from '../../utils/defaultData';

function AccountModal({ isOpen, onClose, accounts, transactions, onAddAccount, onDeleteAccount }) {
  // Stato del form per nuovo conto
  const [formData, setFormData] = useState({
    name: '',
    type: 'current',
    initialBalance: '0'
  });

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
    
    // Crea l'oggetto conto
    const account = {
      name: formData.name,
      type: formData.type,
      initialBalance: parseFloat(formData.initialBalance)
    };
    
    // Chiama la funzione di aggiunta
    onAddAccount(account);
    
    // Reset del form
    setFormData({
      name: '',
      type: 'current',
      initialBalance: '0'
    });
  };

  // Se il modal non è aperto, non renderizza nulla
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Gestisci Conti</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        {/* Lista dei conti esistenti */}
        <div style={{ display: 'grid', gap: '15px', marginBottom: '30px' }}>
          {accounts.map(acc => {
            const balance = calculateAccountBalance(acc.id, accounts, transactions);
            
            return (
              <div
                key={acc.id}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '15px',
                  background: '#f9fafb',
                  borderRadius: '10px'
                }}
              >
                <div>
                  <strong>{acc.name}</strong>
                  <span style={{ color: '#6b7280', fontSize: '14px', marginLeft: '10px' }}>
                    ({accountTypeLabels[acc.type]})
                  </span>
                  <div style={{ color: '#667eea', fontWeight: 'bold', marginTop: '5px' }}>
                    €{balance.toFixed(2)}
                  </div>
                </div>
                <button
                  className="btn-danger"
                  onClick={() => onDeleteAccount(acc.id)}
                >
                  Elimina
                </button>
              </div>
            );
          })}
        </div>

        {/* Form per aggiungere nuovo conto */}
        <h3 style={{ marginTop: '30px', marginBottom: '15px' }}>Aggiungi Nuovo Conto</h3>
        <form onSubmit={handleSubmit}>
          {/* Nome Conto */}
          <div className="form-group">
            <label>Nome Conto</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>

          {/* Tipo e Saldo Iniziale */}
          <div className="form-row">
            <div className="form-group">
              <label>Tipo</label>
              <select
                name="type"
                value={formData.type}
                onChange={handleChange}
                required
              >
                <option value="current">Conto Corrente</option>
                <option value="savings">Risparmio</option>
                <option value="investment">Investimento</option>
              </select>
            </div>

            <div className="form-group">
              <label>Saldo Iniziale (€)</label>
              <input
                type="number"
                name="initialBalance"
                value={formData.initialBalance}
                onChange={handleChange}
                step="0.01"
                required
              />
            </div>
          </div>

          {/* Pulsante submit */}
          <button type="submit" className="btn btn-info" style={{ width: '100%' }}>
            Aggiungi Conto
          </button>
        </form>
      </div>
    </div>
  );
}

export default AccountModal;
