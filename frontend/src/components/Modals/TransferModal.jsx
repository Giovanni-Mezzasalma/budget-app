/**
 * TRANSFER MODAL COMPONENT
 * Modal per aggiungere un trasferimento tra conti
 */

import React, { useState } from 'react';

function TransferModal({ isOpen, onClose, onSave, accounts }) {
  // Stato del form
  const [formData, setFormData] = useState({
    date: new Date().toISOString().split('T')[0],
    operationType: 'Trasferimento',
    fromAccount: '',
    toAccount: '',
    amount: '',
    description: ''
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
    
    // Validazione: i conti devono essere diversi
    if (formData.fromAccount === formData.toAccount) {
      alert('I conti di origine e destinazione devono essere diversi');
      return;
    }
    
    // Crea l'oggetto trasferimento
    const transfer = {
      ...formData,
      fromAccount: parseInt(formData.fromAccount),
      toAccount: parseInt(formData.toAccount),
      amount: parseFloat(formData.amount)
    };
    
    // Chiama la funzione di salvataggio
    onSave(transfer);
    
    // Reset del form
    setFormData({
      date: new Date().toISOString().split('T')[0],
      operationType: 'Trasferimento',
      fromAccount: '',
      toAccount: '',
      amount: '',
      description: ''
    });
  };

  // Se il modal non è aperto, non renderizza nulla
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Nuovo Trasferimento</h2>
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

          {/* Tipo Operazione */}
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

          {/* Da Conto e A Conto */}
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
