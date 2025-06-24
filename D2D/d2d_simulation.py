import socket
import threading
import time
import random
import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table

console = Console()

# --- Configuración de Red ---
UDP_IP = "0.0.0.0"  # Escuchar en todas las interfaces
BROADCAST_IP = "255.255.255.255" # IP de broadcast
UDP_PORT = 12345
DEVICE_ID = os.getenv("DEVICE_ID", f"Device-{random.randint(1000, 9999)}")

# --- Estado del Dispositivo ---
known_devices = {}

def update_display():
    """Genera la tabla para la visualización en vivo."""
    table = Table(title=f"[bold]Red D2D - Vista desde [cyan]{DEVICE_ID}[/cyan][/bold]", show_header=True, header_style="bold magenta")
    table.add_column("ID Dispositivo", style="dim", width=20)
    table.add_column("Último Mensaje")
    table.add_column("Timestamp", justify="center")

    for device, info in list(known_devices.items()):
        table.add_row(device, info['message'], time.strftime('%H:%M:%S', time.localtime(info['timestamp'])))
    
    return table

def listener():
    """Escucha mensajes UDP de otros dispositivos."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = json.loads(data.decode())
            sender_id = message.get("device_id")

            if sender_id and sender_id != DEVICE_ID:
                known_devices[sender_id] = {
                    "message": message.get("content"),
                    "timestamp": time.time()
                }
        except (json.JSONDecodeError, KeyError):
            pass # Ignorar mensajes mal formados
        except Exception as e:
            console.print(f"[red]Error en listener: {e}[/red]")

def broadcaster():
    """Envía mensajes de broadcast a la red."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    messages = [
        "Hola a todos, ¿alguien me escucha?",
        "Compartiendo mi estado: todo OK.",
        "Detectada una anomalía en mi sector.",
        "La temperatura actual es de 25°C.",
        "Batería al 80%."
    ]

    while True:
        try:
            message_content = random.choice(messages)
            message = {
                "device_id": DEVICE_ID,
                "content": message_content
            }
            sock.sendto(json.dumps(message).encode(), (BROADCAST_IP, UDP_PORT))
            time.sleep(random.randint(5, 15))
        except Exception as e:
            console.print(f"[red]Error en broadcaster: {e}[/red]")

if __name__ == "__main__":
    console.print(Panel(f"[bold green]Iniciando dispositivo [cyan]{DEVICE_ID}[/cyan] en la red D2D...[/bold green]", border_style="green"))

    listener_thread = threading.Thread(target=listener, daemon=True)
    broadcaster_thread = threading.Thread(target=broadcaster, daemon=True)

    listener_thread.start()
    broadcaster_thread.start()

    try:
        with Live(update_display(), screen=True, redirect_stderr=False) as live:
            while True:
                time.sleep(1)
                # Limpiar dispositivos inactivos (más de 60s)
                current_time = time.time()
                inactive_devices = [dev for dev, info in known_devices.items() if current_time - info['timestamp'] > 60]
                for dev in inactive_devices:
                    del known_devices[dev]
                live.update(update_display())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Cerrando dispositivo...[/bold yellow]")