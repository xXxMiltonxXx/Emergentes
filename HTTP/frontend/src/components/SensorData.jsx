import { useState, useEffect } from 'preact/hooks';

export default function SensorData({ initialData, apiUrl }) {
  const [data, setData] = useState(initialData);
  const [error, setError] = useState(null);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const newData = await response.json();
        setData(newData);
        setError(null);
      } catch (e) {
        console.error("Failed to fetch data:", e);
        setError("No se pudo conectar con la API. Verifique que el servicio esté en ejecución.");
      }
    }, 5000); // Actualiza cada 5 segundos

    return () => clearInterval(interval);
  }, [apiUrl]);

  return (
    <div className="sensor-data-container">
      {error && <p className="error-message">{error}</p>}
      {!error && data.length === 0 && (
        <p className="loading-message">Esperando datos de los sensores...</p>
      )}
      {!error && data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Temperatura</th>
              <th>Humedad</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{new Date(item.timestamp).toLocaleString()}</td>
                <td>{item.temperature.toFixed(2)} °C</td>
                <td>{item.humidity.toFixed(2)} %</td>
              </tr>
            )).reverse() /* Muestra los más recientes primero */}
          </tbody>
        </table>
      )}
    </div>
  );
}