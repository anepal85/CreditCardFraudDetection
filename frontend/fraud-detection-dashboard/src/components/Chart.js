import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function Chart({ testData, predictions }) {
  // Prepare data for the chart
  const labels = testData.map((_, index) => `Transaction ${index + 1}`);
  const actualClasses = testData.map((row) => row.Class);
  const predictedClasses = predictions;

  const data = {
    labels,
    datasets: [
      {
        label: "Actual Class",
        data: actualClasses,
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
      {
        label: "Predicted Class",
        data: predictedClasses,
        backgroundColor: "rgba(255, 99, 132, 0.6)",
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Actual vs Predicted Fraud Detection",
      },
    },
  };

  return (
    <div className="chart">
      <Bar data={data} options={options} />
    </div>
  );
}

export default Chart;