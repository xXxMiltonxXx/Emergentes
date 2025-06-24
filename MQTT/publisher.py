import paho.mqtt.client as mqtt
import time
import json
import random
from rich.console import Console
from rich.panel import Panel

# --- Configuración MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "iot/home/livingroom/sensor"
CLIENT_ID = f"publisher-{random.randint(0, 1000)}"

console = Console()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        console.print(Panel(f"[bold green]Conectado exitosamente al Broker MQTT![/bold green] (ID: {CLIENT_ID})", title="Estado del Publicador", border_style="green"))
    else:
        console.print(f"[bold red]Fallo al conectar, código de retorno: {rc}[/bold red]")

def on_publish(client, userdata, mid):
    console.log(f"Mensaje {mid} publicado.")

def run():
    client = mqtt.Client(client_id=CLIENT_ID)
    client.on_connect = on_connect
    client.on_publish = on_publish
    
    try:
        client.connect(BROKER_ADDRESS, BROKER_PORT)
    except Exception as e:
        console.print(f"[bold red]Error de conexión:[/bold red] {e}")
        return

    client.loop_start()

    try:
        while True:
            temperature = round(random.uniform(20.0, 28.0), 2)
            humidity = round(random.uniform(40.0, 60.0), 2)
            payload = json.dumps({"temperature": temperature, "humidity": humidity})
            
            result = client.publish(TOPIC, payload)
            status = result[0]
            
            if status == 0:
                console.print(f"Enviando datos: [cyan]Temp: {temperature}°C, Hum: {humidity}%[/cyan] al topic [yellow]'{TOPIC}'[/yellow]")
            else:
                console.print(f"[red]Fallo al enviar mensaje al topic.[/red]")

            time.sleep(5)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Publicación detenida por el usuario.[/bold yellow]")
    finally:
        client.loop_stop()
        client.disconnect()
        console.print("[bold blue]Desconectado del broker.[/bold blue]")

if __name__ == '__main__':
    run()