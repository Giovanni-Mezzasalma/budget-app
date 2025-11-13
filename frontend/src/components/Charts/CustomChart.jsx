/**
 * CUSTOM CHART COMPONENT
 * Componente che renderizza un grafico personalizzato
 * in base alla configurazione salvata dall'utente
 */

import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line, Bar, Pie, Doughnut } from 'react-chartjs-2';
import { getChartData } from '../../utils/chartUtils';

// Registra tutti i componenti di Chart.js necessari
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

function CustomChart({ config, transactions, accounts }) {
  // Ottiene i dati del grafico in base alla configurazione
  const chartData = getChartData(config, transactions, accounts);

  // Opzioni base del grafico
  const baseOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: config.type === 'pie' || config.type === 'doughnut' ? 'right' : 'top'
      }
    }
  };

  // Aggiunge le scale solo per grafici non circolari
  const options = config.type === 'pie' || config.type === 'doughnut'
    ? baseOptions
    : {
        ...baseOptions,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };

  // Seleziona il componente del grafico in base al tipo
  const renderChart = () => {
    switch (config.type) {
      case 'line':
        return <Line data={chartData} options={options} />;
      case 'bar':
        return <Bar data={chartData} options={options} />;
      case 'pie':
        return <Pie data={chartData} options={options} />;
      case 'doughnut':
        return <Doughnut data={chartData} options={options} />;
      default:
        return <Line data={chartData} options={options} />;
    }
  };

  return (
    <div className="chart-container">
      {renderChart()}
    </div>
  );
}

export default CustomChart;
