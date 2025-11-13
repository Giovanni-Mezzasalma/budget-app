/**
 * PIE CHART COMPONENT
 * Grafico a torta che mostra la distribuzione delle spese
 * per categoria (top 8 categorie)
 */

import React from 'react';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js';
import { Pie } from 'react-chartjs-2';
import { calculateCategoryTotals } from '../../utils/calculations';

// Registra i componenti di Chart.js necessari
ChartJS.register(ArcElement, Tooltip, Legend);

function PieChart({ transactions }) {
  // Calcola i totali per categoria
  const categoryTotals = calculateCategoryTotals(transactions);
  
  // Ordina e prende le prime 8 categorie
  const sorted = Object.entries(categoryTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8);

  // Se non ci sono dati, non renderizza il grafico
  if (sorted.length === 0) {
    return (
      <div className="chart-container" style={{ height: '350px' }}>
        <div className="empty-state">
          <h3>Nessun dato disponibile</h3>
        </div>
      </div>
    );
  }

  // Configurazione dei dati per il grafico
  const chartData = {
    labels: sorted.map(([cat]) => cat),
    datasets: [{
      data: sorted.map(([_, amount]) => amount),
      backgroundColor: [
        '#667eea', '#764ba2', '#f093fb', '#4facfe',
        '#43e97b', '#fa709a', '#fee140', '#30cfd0'
      ]
    }]
  };

  // Opzioni di configurazione del grafico
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'right'
      }
    }
  };

  return (
    <div className="chart-container" style={{ height: '350px' }}>
      <Pie data={chartData} options={options} />
    </div>
  );
}

export default PieChart;
