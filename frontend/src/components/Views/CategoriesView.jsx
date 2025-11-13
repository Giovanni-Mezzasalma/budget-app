/**
 * CATEGORIES VIEW COMPONENT
 * Vista che mostra le spese raggruppate per categoria
 * per il mese selezionato
 */

import React from 'react';
import { filterTransactionsByMonth, calculateCategoryTotals } from '../../utils/calculations';

function CategoriesView({ transactions, selectedMonth, selectedYear }) {
  // Filtra le transazioni per il mese selezionato
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Calcola i totali per categoria
  const categoryTotals = calculateCategoryTotals(filteredTransactions);
  
  // Ordina le categorie per importo decrescente
  const sortedCategories = Object.entries(categoryTotals).sort((a, b) => b[1] - a[1]);

  // Se non ci sono spese, mostra messaggio vuoto
  if (sortedCategories.length === 0) {
    return (
      <div className="card">
        <h2>Spese per Categoria</h2>
        <div className="empty-state">
          <h3>Nessuna spesa</h3>
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Spese per Categoria</h2>
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', 
        gap: '15px' 
      }}>
        {sortedCategories.map(([category, amount]) => (
          <div
            key={category}
            style={{
              background: '#f9fafb',
              padding: '20px',
              borderRadius: '10px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }}
          >
            {/* Nome categoria */}
            <span style={{ fontWeight: 600 }}>{category}</span>
            
            {/* Importo totale */}
            <span style={{ 
              fontWeight: 'bold', 
              color: '#ef4444', 
              fontSize: '18px' 
            }}>
              €{amount.toFixed(2)}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CategoriesView;
