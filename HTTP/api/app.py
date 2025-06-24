from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# --- Almacenamiento en Memoria ---
# En un caso real, esto sería una base de datos (ej. SQLite, PostgreSQL).
sensor_data = {
    'temperature': 22.5,
    'humidity': 45.8,
    'last_updated': datetime.datetime.now().isoformat()
}

# --- Endpoints de la API ---

@app.route('/api/data', methods=['GET'])
def get_data():
    """Devuelve los últimos datos del sensor."""
    return jsonify(sensor_data)

@app.route('/api/data', methods=['POST'])
def receive_data():
    """Recibe nuevos datos de un dispositivo IoT."""
    if not request.json or not 'temperature' in request.json or not 'humidity' in request.json:
        return jsonify({'error': 'Invalid data format'}), 400

    global sensor_data
    sensor_data = {
        'temperature': request.json['temperature'],
        'humidity': request.json['humidity'],
        'last_updated': datetime.datetime.now().isoformat()
    }
    return jsonify({'message': 'Data received successfully'}), 201

# --- Simulación (Opcional, para desarrollo) ---
# Este endpoint simula una actualización de datos como si viniera de un sensor.
@app.route('/api/simulate_update', methods=['POST'])
def simulate_update():
    """Simula la llegada de nuevos datos."""
    global sensor_data
    sensor_data = {
        'temperature': round(random.uniform(18.0, 28.0), 2),
        'humidity': round(random.uniform(30.0, 60.0), 2),
        'last_updated': datetime.datetime.now().isoformat()
    }
    return jsonify({'message': 'Simulated data updated'}), 200

if __name__ == '__main__':
    # Escucha en todas las interfaces de red, crucial para Docker
    app.run(host='0.0.0.0', port=5000, debug=True)