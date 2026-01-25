/**
 * TRANSFER MODAL COMPONENT
 * Modal for adding a transfer between accounts
 */

import React, { useState } from 'react';

function TransferModal({ isOpen, onClose, onSave, accounts }) {
  // Form Status
  const [formData, setFormData] = useState({
    date: new Date().toISOString().split('T')[0],
    operationType: 'Trasferimento',
    fromAccount: '',
    toAccount: '',
    amount: '',
    description: ''
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
    
    // Validation: Accounts must be different
    if (formData.fromAccount === formData.toAccount) {
      alert('I conti di origine e destinazione devono essere diversi');
      return;
    }
    
    // Create the transfer object
    const transfer = {
      ...formData,
      fromAccount: parseInt(formData.fromAccount),
      toAccount: parseInt(formData.toAccount),
      amount: parseFloat(formData.amount)
    };
    
    // Call the save function
    onSave(transfer);
    
    // Reset the form
    setFormData({
      date: new Date().toISOString().split('T')[0],
      operationType: 'Trasferimento',
      fromAccount: '',
      toAccount: '',
      amount: '',
      description: ''
    });
  };

  // If the modal is not open, it does not render anything
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Nuovo Trasferimento</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        <form onSubmit={handleSubmit}>
          {/* Date */}
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

          {/* Operation Type */}
          <div className="form-group">
            <label>Tipo Operazione</label>
            <select
              name="operationType"
              value={formData.operationType}
              onChange={handleChange}
              required
            >
              <option value="Trasferimento">Trasferimento tra conti</option>
              <option value="Risparmio">Verso Risparmio</option>
              <option value="Investimenti">Verso Investimenti</option>
            </select>
          </div>

          {/* From Account and To Account */}
          <div className="form-row">
            <div className="form-group">
              <label>Da Conto</label>
              <select
                name="fromAccount"
                value={formData.fromAccount}
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

            <div className="form-group">
              <label>A Conto</label>
              <select
                name="toAccount"
                value={formData.toAccount}
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

          {/* Amount */}
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

          {/* Description */}
          <div className="form-group">
            <label>Descrizione (opzionale)</label>
            <input
              type="text"
              name="description"
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          {/* Buttons */}
          <div style={{ display: 'flex', gap: '10px' }}>
            <button type="submit" className="btn btn-success" style={{ flex: 1 }}>
              Trasferisci
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

export default TransferModal;
