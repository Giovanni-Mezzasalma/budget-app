/**
 * CUSTOM CHARTS VIEW COMPONENT
 * View for managing and displaying custom graphs
 */

import React from 'react';
import CustomChart from '../Charts/CustomChart';

function CustomChartsView({ savedCharts, transactions, accounts, onCreateChart, onEditChart, onDeleteChart }) {
  
  // If there are no saved graphs, show blank message
  if (savedCharts.length === 0) {
    return (
      <div className="card">
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          marginBottom: '20px' 
        }}>
          <h2>📈 Grafici Personalizzati</h2>
          <button className="btn btn-primary" onClick={onCreateChart}>
            + Nuovo Grafico
          </button>
        </div>
        
        <div className="empty-state">
          <h3>Nessun grafico personalizzato</h3>
          <p>Clicca su "+ Nuovo Grafico" per iniziare</p>
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        marginBottom: '20px' 
      }}>
        <h2>📈 Grafici Personalizzati</h2>
        <button className="btn btn-primary" onClick={onCreateChart}>
          + Nuovo Grafico
        </button>
      </div>

      {/* Render all saved graphs */}
      {savedCharts.map((chart) => (
        <div key={chart.id} className="custom-chart-card">
          {/* Chart header with title and buttons */}
          <div className="chart-header">
            <div className="chart-title">{chart.title}</div>
            <div>
              <button 
                className="btn btn-info btn-small" 
                onClick={() => onEditChart(chart.id)}
              >
                ✏️ Modifica
              </button>
              <button 
                className="btn-danger btn-small" 
                onClick={() => onDeleteChart(chart.id)}
                style={{ marginLeft: '10px' }}
              >
                🗑️ Elimina
              </button>
            </div>
          </div>

          {/* Chart Component */}
          <CustomChart 
            config={chart} 
            transactions={transactions} 
            accounts={accounts} 
          />
        </div>
      ))}
    </div>
  );
}

export default CustomChartsView;
