import paho.mqtt.client as mqtt
import time
import random
import json
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- Configuración del Broker MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "d2c/sensor/data"

# --- Simulación del Dispositivo ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        console.print(Panel(f"[bold green]Conectado exitosamente al broker MQTT en {BROKER_ADDRESS}[/bold green]", title="[yellow]Estado de Conexión[/yellow]"))
    else:
        console.print(Panel(f"[bold red]Error al conectar, código de retorno: {rc}[/bold red]", title="[red]Error de Conexión[/red]"))

def simulate_device(device_id):
    client = mqtt.Client(client_id=f"device-{device_id}")
    client.on_connect = on_connect

    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    except Exception as e:
        console.print(Panel(f"[bold red]No se pudo conectar al broker: {e}[/bold red]", title="[red]Error Crítico[/red]"))
        return

    client.loop_start()

    while True:
        try:
            temperature = round(random.uniform(20.0, 30.0), 2)
            humidity = round(random.uniform(40.0, 60.0), 2)
            
            payload = {
                "deviceId": device_id,
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": time.time()
            }
            
            json_payload = json.dumps(payload)
            client.publish(TOPIC, json_payload)
            
            console.print(Panel(f"[cyan]Datos enviados:[/cyan] [bold]{json_payload}[/bold]", title=f"[green]Dispositivo {device_id}[/green]"))
            
            time.sleep(random.randint(5, 10))

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Simulación detenida por el usuario.[/bold yellow]")
            break
        except Exception as e:
            console.print(Panel(f"[bold red]Ocurrió un error: {e}[/bold red]", title="[red]Error en Ejecución[/red]"))
            time.sleep(5)

    client.loop_stop()
    client.disconnect()
    console.print("[bold blue]Desconectado del broker MQTT.[/bold blue]")

if __name__ == "__main__":
    device_id = f"sensor-{random.randint(100, 999)}"
    simulate_device(device_id)