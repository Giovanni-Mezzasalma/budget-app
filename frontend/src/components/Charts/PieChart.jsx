/**
 * PIE CHART COMPONENT
 * Pie chart showing the distribution of expenses
 * by category (top 8 categories)
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

// Register the necessary Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

function PieChart({ transactions }) {
  // Calculate totals by category
  const categoryTotals = calculateCategoryTotals(transactions);
  
  // Sort and get the first 8 categories
  const sorted = Object.entries(categoryTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8);

  // If there is no data, do not render the graph
  if (sorted.length === 0) {
    return (
      <div className="chart-container" style={{ height: '350px' }}>
        <div className="empty-state">
          <h3>Nessun dato disponibile</h3>
        </div>
      </div>
    );
  }

  // Configuring the data for the chart
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

  // Chart configuration options
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
