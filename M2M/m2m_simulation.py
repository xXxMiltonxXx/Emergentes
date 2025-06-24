import time
import random
import os
from rich.console import Console
from rich.table import Table

console = Console()

def simulate_device(device_id):
    """Simula el comportamiento de un dispositivo M2M con una salida visualmente atractiva."""
    console.print(f"[bold cyan][Dispositivo {device_id}] Iniciando simulación...[/bold cyan]")

    while True:
        # Simular la recolección de datos
        temperature = round(random.uniform(15.0, 35.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        status = random.choice(["[green]activo[/green]", "[yellow]inactivo[/yellow]", "[red]mantenimiento[/red]"])

        # Crear una tabla para mostrar los datos de forma organizada
        table = Table(title=f"[bold]Datos del Dispositivo {device_id}[/bold]", show_header=True, header_style="bold magenta")
        table.add_column("Métrica", style="dim", width=12)
        table.add_column("Valor")

        table.add_row("Temperatura", f"{temperature}°C")
        table.add_row("Humedad", f"{humidity}%")
        table.add_row("Estado", status)

        console.print(table)

        # Simular el envío de datos
        if random.random() < 0.8:
            console.print(f"[bold blue][Dispositivo {device_id}] Enviando datos...[/bold blue]")
        else:
            console.print(f"[bold yellow][Dispositivo {device_id}] No hay datos nuevos para enviar.[/bold yellow]")

        console.print("-" * 40)
        time.sleep(random.randint(3, 6))

if __name__ == "__main__":
    console.print("[bold green]Iniciando simulación M2M...[/bold green]")
    device_id = os.getenv("DEVICE_ID", "A001")
    simulate_device(device_id)