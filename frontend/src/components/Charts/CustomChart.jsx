/**
 * CUSTOM CHART COMPONENT
 * Component that renders a custom chart
 * based on the user's saved configuration
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

// Register all necessary Chart.js components
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
  // Gets the chart data based on the configuration
  const chartData = getChartData(config, transactions, accounts);

  // Basic chart options
  const baseOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: config.type === 'pie' || config.type === 'doughnut' ? 'right' : 'top'
      }
    }
  };

  // Add scales only for non-circular graphs
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

  // Select the chart component based on its type
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
