/**
 * CATEGORY CHART COMPONENT
 * Bar chart showing expense comparison
 * by category (top 10 categories)
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

// Register the necessary Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function CategoryChart({ transactions }) {
// Calculate totals by category
  const categoryTotals = calculateCategoryTotals(transactions);
  
  // Sort and get the first 10 categories
  const sorted = Object.entries(categoryTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  // If there is no data, do not render the graph
  if (sorted.length === 0) {
    return (
      <div className="chart-container">
        <div className="empty-state">
          <h3>Nessun dato disponibile</h3>
        </div>
      </div>
    );
  }

  // Configuring data for the chart
  const chartData = {
    labels: sorted.map(([cat]) => cat),
    datasets: [{
      label: 'Spesa (€)',
      data: sorted.map(([_, amount]) => amount),
      backgroundColor: '#667eea'
    }]
  };

  // Chart configuration options
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
