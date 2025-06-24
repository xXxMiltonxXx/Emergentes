import requests
import time
import random
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- Configuración ---
API_URL = os.getenv("API_URL", "http://localhost:5000/api/data")
DEVICE_ID = os.getenv("DEVICE_ID", f"SimDevice-{random.randint(1000, 9999)}")

def send_data():
    """Genera datos y los envía a la API."""
    temperature = round(random.uniform(18.0, 28.0), 2)
    humidity = round(random.uniform(30.0, 60.0), 2)
    payload = {
        'temperature': temperature,
        'humidity': humidity
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)
        if response.status_code == 201:
            console.print(f"[green]>[/green] [bold]({DEVICE_ID})[/bold] Datos enviados exitosamente: Temp: {temperature}°C, Hum: {humidity}%")
        else:
            console.print(f"[red]Error al enviar datos:[/red] {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Fallo de conexión con la API en {API_URL}:[/bold red] {e}")

if __name__ == "__main__":
    console.print(Panel(f"[bold]Iniciando Simulador de Dispositivo IoT[/bold]\nID: [cyan]{DEVICE_ID}[/cyan]\nAPI Target: [yellow]{API_URL}[/yellow]", title="[green]Device Simulator[/green]"))
    while True:
        send_data()
        sleep_time = random.randint(5, 15)
        console.log(f"Esperando {sleep_time} segundos para el próximo envío...")
        time.sleep(sleep_time)