/**
 * ACCOUNT MODAL COMPONENT
 * Modal for managing bank accounts:
 * - View existing accounts
 * - Add new accounts
 * - Delete accounts
 */

import React, { useState } from 'react';
import { calculateAccountBalance } from '../../utils/calculations';
import { accountTypeLabels } from '../../utils/defaultData';

function AccountModal({ isOpen, onClose, accounts, transactions, onAddAccount, onDeleteAccount }) {
  // New account form status
  const [formData, setFormData] = useState({
    name: '',
    type: 'current',
    initialBalance: '0'
  });

  /**
   * Manages changes in form fields
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  /**
   * Manages form submission
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Create the account object
    const account = {
      name: formData.name,
      type: formData.type,
      initialBalance: parseFloat(formData.initialBalance)
    };
    
    // Call the add function
    onAddAccount(account);
    
    // Reset the form
    setFormData({
      name: '',
      type: 'current',
      initialBalance: '0'
    });
  };

  // If the modal is not open, it does not render anything
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Gestisci Conti</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        {/* List of existing accounts */}
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

        {/* Form to add new account */}
        <h3 style={{ marginTop: '30px', marginBottom: '15px' }}>Aggiungi Nuovo Conto</h3>
        <form onSubmit={handleSubmit}>
          {/* Account Name */}
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

          {/* Type and Initial Balance */}
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

          {/* Submit button */}
          <button type="submit" className="btn btn-info" style={{ width: '100%' }}>
            Aggiungi Conto
          </button>
        </form>
      </div>
    </div>
  );
}

export default AccountModal;
