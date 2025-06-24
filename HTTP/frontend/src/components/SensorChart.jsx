import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const SensorChart = ({ apiUrl }) => {
  const [sensorData, setSensorData] = useState([]);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }
      const data = await response.json();
      setSensorData(prevData => [...prevData, data].slice(-20)); // Keep last 20 data points
      setError(null);
    } catch (err) {
      setError(err.message);
      console.error("Failed to fetch sensor data:", err);
    }
  };

  useEffect(() => {
    fetchData(); // Fetch initial data
    const interval = setInterval(fetchData, 5000); // Fetch data every 5 seconds
    return () => clearInterval(interval); // Cleanup on component unmount
  }, [apiUrl]);

  const chartData = {
    labels: sensorData.map(d => new Date(d.last_updated).toLocaleTimeString()),
    datasets: [
      {
        label: 'Temperature (°C)',
        data: sensorData.map(d => d.temperature),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y',
      },
      {
        label: 'Humidity (%)',
        data: sensorData.map(d => d.humidity),
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        yAxisID: 'y1',
      },
    ],
  };

  const options = {
    responsive: true,
    interaction: {
      mode: 'index',
      intersect: false,
    },
    stacked: false,
    plugins: {
      title: {
        display: true,
        text: 'Live Sensor Data',
      },
    },
    scales: {
      y: {
        type: 'linear',
        display: true,
        position: 'left',
        title: {
            display: true,
            text: 'Temperature (°C)'
        }
      },
      y1: {
        type: 'linear',
        display: true,
        position: 'right',
        title: {
            display: true,
            text: 'Humidity (%)'
        },
        grid: {
          drawOnChartArea: false, // only draw grid lines for the first Y axis
        },
      },
    },
  };

  return (
    <div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <Line options={options} data={chartData} />
    </div>
  );
};

export default SensorChart;