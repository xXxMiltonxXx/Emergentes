import paho.mqtt.client as mqtt
import json
from rich.console import Console
from rich.table import Table
from rich.live import Live
from datetime import datetime

console = Console()

# --- Configuración del Broker MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "d2c/sensor/data"

# --- Almacenamiento en memoria de los datos ---
device_data = {}

def generate_table() -> Table:
    """Genera una tabla de Rich para mostrar los datos de los dispositivos."""
    table = Table(title="[bold]Datos de Sensores en la Nube[/bold]", show_header=True, header_style="bold blue")
    table.add_column("ID Dispositivo", style="dim", width=15)
    table.add_column("Temperatura", justify="right")
    table.add_column("Humedad", justify="right")
    table.add_column("Última Actualización", justify="center", style="magenta")

    for device_id, data in device_data.items():
        timestamp = datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        table.add_row(
            device_id,
            f"{data['temperature']}°C",
            f"{data['humidity']}%",
            timestamp
        )
    return table

# --- Lógica del Cliente MQTT ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        console.print("[bold green]Servicio en la nube conectado al broker MQTT.[/bold green]")
        client.subscribe(TOPIC)
        console.print(f"[cyan]Suscrito al tópico:[/cyan] [bold]{TOPIC}[/bold]")
    else:
        console.print(f"[bold red]Error de conexión con código: {rc}[/bold red]")

def on_message(client, userdata, msg):
    """Callback que se ejecuta cuando se recibe un mensaje."""
    try:
        payload = json.loads(msg.payload.decode())
        device_id = payload.get("deviceId")
        
        if device_id:
            device_data[device_id] = payload

    except json.JSONDecodeError:
        console.print("[bold red]Error al decodificar el mensaje JSON.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error procesando el mensaje: {e}[/bold red]")

def run_cloud_service():
    client = mqtt.Client(client_id="cloud-service-subscriber")
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    except Exception as e:
        console.print(f"[bold red]No se pudo conectar al broker: {e}[/bold red]")
        return

    client.loop_start()

    try:
        with Live(generate_table(), screen=True, redirect_stderr=False) as live:
            while True:
                time.sleep(1)
                live.update(generate_table())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Servicio en la nube detenido.[/bold yellow]")
    finally:
        client.loop_stop()
        client.disconnect()
        console.print("[bold blue]Desconectado del broker MQTT.[/bold blue]")

if __name__ == "__main__":
    import time
    run_cloud_service()