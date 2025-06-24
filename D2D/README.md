# Simulación D2D (Device-to-Device) con Sockets UDP y Docker

Este proyecto demuestra una comunicación Device-to-Device (D2D) en una red local. Los dispositivos se descubren y comunican entre sí mediante mensajes de broadcast UDP, sin necesidad de un servidor o broker central.

## Características

- **Comunicación Descentralizada**: No depende de un punto central de fallo.
- **Sockets UDP**: Utiliza broadcast UDP para enviar mensajes a todos los dispositivos en la red.
- **Visualización en Tiempo Real**: Cada dispositivo tiene su propia vista de la red, mostrando los mensajes que recibe de otros nodos, gracias a la librería `rich`.
- **Dockerizado**: Se utiliza Docker Compose para lanzar múltiples dispositivos que forman la red D2D.

**Nota Importante sobre `network_mode: "host"`**: Este modo es crucial para que los contenedores puedan enviar y recibir paquetes de broadcast en la red local del anfitrión. Puede tener implicaciones de seguridad y no funcionar en todos los entornos de Docker (especialmente en macOS y Windows con WSL2 puede requerir configuración adicional).

## Estructura del Proyecto

```
.
├── Dockerfile
├── d2d_simulation.py
├── docker-compose.yml
└── requirements.txt
```

## Cómo Ejecutar la Simulación

1.  **Requisitos Previos**:
    -   Tener Docker y Docker Compose instalados.

2.  **Construir y Ejecutar**:
    Abre una terminal en el directorio raíz del proyecto y ejecuta:

    ```bash
    docker-compose up --build
    ```

3.  **Ver la Simulación**:
    La salida de `docker-compose` mostrará los logs de todos los contenedores. Sin embargo, para una mejor visualización, es recomendable abrir terminales separadas para cada dispositivo y ver sus logs individualmente:

    ```bash
    # En una terminal
    docker logs -f d2d-node-1

    # En otra terminal
    docker logs -f d2d-node-2

    # Y en una tercera
    docker logs -f d2d-node-3
    ```

    En cada terminal, verás una tabla que se actualiza con los mensajes que ese dispositivo específico está recibiendo de los otros.

## Ejecución en Múltiples Dispositivos (Multi-Host)

Para probar la comunicación entre diferentes computadoras en la misma red local, sigue estos pasos en cada máquina:

1.  **Clona el Proyecto**: Asegúrate de tener los archivos del proyecto en cada computadora.

2.  **Construye la Imagen Docker**:
    En una terminal, en la raíz del proyecto, ejecuta:
    ```bash
    docker build -t d2d-node .
    ```

3.  **Ejecuta un Contenedor**:
    Inicia un contenedor en cada máquina. **Asegúrate de asignar un `DEVICE_ID` único para cada una**.

    En la **Máquina 1**:
    ```bash
    docker run --rm --network="host" -e DEVICE_ID="PC-Oficina-01" --name d2d-pc-1 d2d-node
    ```

    En la **Máquina 2**:
    ```bash
    docker run --rm --network="host" -e DEVICE_ID="Laptop-Sala-02" --name d2d-pc-2 d2d-node
    ```

    Ahora, los dispositivos en las diferentes máquinas deberían verse entre sí en sus respectivas terminales.

    **Nota sobre Firewalls**: Si los dispositivos no se comunican, asegúrate de que el firewall de tu sistema operativo o de tu red no esté bloqueando el tráfico UDP en el puerto `12345`.

4.  **Detener la Simulación**:
    Presiona `Ctrl+C` en la terminal donde se está ejecutando `docker-compose`.

## Descripción de los Archivos

-   `d2d_simulation.py`: El script principal que implementa un nodo de la red D2D. Escucha mensajes de otros y envía los suyos propios periódicamente.
-   `Dockerfile`: Define la imagen Docker para un nodo D2D.
-   `docker-compose.yml`: Orquesta la creación de tres nodos D2D para simular la red.
-   `requirements.txt`: Contiene la dependencia de Python (`rich`).