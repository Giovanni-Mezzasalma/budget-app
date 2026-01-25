/**
 * CATEGORIES VIEW COMPONENT
 * View showing expenses grouped by category
 * for the selected month
 */

import React from 'react';
import { filterTransactionsByMonth, calculateCategoryTotals } from '../../utils/calculations';

function CategoriesView({ transactions, selectedMonth, selectedYear }) {
  // Filter transactions for the selected month
  const filteredTransactions = filterTransactionsByMonth(transactions, selectedMonth, selectedYear);
  
  // Calculate totals by category
  const categoryTotals = calculateCategoryTotals(filteredTransactions);
  
  // Sort categories by descending amount
  const sortedCategories = Object.entries(categoryTotals).sort((a, b) => b[1] - a[1]);

  // If there are no charges, show empty message
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
            {/* Category Name */}
            <span style={{ fontWeight: 600 }}>{category}</span>
            
            {/* Total amount */}
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
