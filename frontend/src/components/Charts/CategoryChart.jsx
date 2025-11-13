/**
 * CATEGORY CHART COMPONENT
 * Grafico a barre che mostra il confronto delle spese
 * per categoria (top 10 categorie)
 */

import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { calculateCategoryTotals } from '../../utils/calculations';

// Registra i componenti di Chart.js necessari
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function CategoryChart({ transactions }) {
  // Calcola i totali per categoria
  const categoryTotals = calculateCategoryTotals(transactions);
  
  // Ordina e prende le prime 10 categorie
  const sorted = Object.entries(categoryTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  // Se non ci sono dati, non renderizza il grafico
  if (sorted.length === 0) {
    return (
      <div className="chart-container">
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
      label: 'Spesa (€)',
      data: sorted.map(([_, amount]) => amount),
      backgroundColor: '#667eea'
    }]
  };

  // Opzioni di configurazione del grafico
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };

  return (
    <div className="chart-container">
      <Bar data={chartData} options={options} />
    </div>
  );
}

export default CategoryChart;
