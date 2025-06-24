import paho.mqtt.client as mqtt
import json
import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

# --- Configuración MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "iot/home/livingroom/sensor"

console = Console()

# --- Almacenamiento de Datos ---
received_data = []

def generate_table() -> Table:
    """Genera una tabla con los datos recibidos."""
    table = Table(title="[bold]Datos del Sensor en Tiempo Real[/bold]", show_header=True, header_style="bold magenta")
    table.add_column("Timestamp", style="dim", width=12)
    table.add_column("Temperatura (°C)", justify="right")
    table.add_column("Humedad (%)", justify="right")

    # Mostrar solo los últimos 10 mensajes
    for data in received_data[-10:]:
        table.add_row(
            data["timestamp"],
            f"[cyan]{data['temperature']}[/cyan]",
            f"[green]{data['humidity']}[/green]"
        )
    return table

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        console.print(Panel("[bold green]Conectado exitosamente al Broker MQTT![/bold green]", title="Estado del Suscriptor", border_style="green"))
        client.subscribe(TOPIC)
        console.print(f"Suscrito al topic: [yellow]'{TOPIC}'[/yellow]")
    else:
        console.print(f"[bold red]Fallo al conectar, código de retorno: {rc}[/bold red]")

def on_message(client, userdata, msg):
    """Callback que se ejecuta cuando se recibe un mensaje."""
    try:
        payload = json.loads(msg.payload.decode())
        temperature = payload.get("temperature")
        humidity = payload.get("humidity")
        timestamp = time.strftime('%H:%M:%S')

        if temperature is not None and humidity is not None:
            received_data.append({
                "timestamp": timestamp,
                "temperature": temperature,
                "humidity": humidity
            })
    except json.JSONDecodeError:
        console.log("[red]Error al decodificar JSON.[/red]")
    except Exception as e:
        console.log(f"[red]Error inesperado: {e}[/red]")

def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    except Exception as e:
        console.print(f"[bold red]Error de conexión:[/bold red] {e}")
        return

    client.loop_start()

    try:
        with Live(generate_table(), screen=True, redirect_stderr=False) as live:
            while True:
                time.sleep(1)
                live.update(generate_table())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Suscripción detenida por el usuario.[/bold yellow]")
    finally:
        client.loop_stop()
        client.disconnect()
        console.print("[bold blue]Desconectado del broker.[/bold blue]")

if __name__ == '__main__':
    run()