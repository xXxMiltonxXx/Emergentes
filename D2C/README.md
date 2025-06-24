# Simulación D2C (Device-to-Cloud) con MQTT y Docker

Este proyecto simula un escenario de IoT donde un dispositivo envía datos de sensores a un servicio en la nube a través del protocolo MQTT. Todo el entorno está contenido en Docker para una fácil ejecución.

## Características

- **Protocolo MQTT**: Utiliza un broker MQTT público (`broker.hivemq.com`) para la comunicación.
- **Visualización Atractiva**: Usa la librería `rich` para mostrar los datos de forma clara y colorida.
- **Dockerizado**: Ambos, el dispositivo y el servicio en la nube, se ejecutan en contenedores Docker separados.

## Estructura del Proyecto

```
.
├── Dockerfile
├── cloud_service.py
├── device_simulation.py
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
    -   **Servicio en la Nube**: En la salida de `docker-compose`, verás una tabla que se actualiza en tiempo real con los datos que llegan del dispositivo.
    -   **Dispositivo**: Verás los paneles que indican los datos que se están enviando al broker MQTT.

4.  **Detener la Simulación**:
    Presiona `Ctrl+C` en la terminal donde se está ejecutando `docker-compose`.

## Descripción de los Archivos

-   `device_simulation.py`: Simula un dispositivo IoT que recolecta datos (temperatura y humedad) y los publica en un tópico MQTT.
-   `cloud_service.py`: Simula un servicio en la nube que se suscribe al tópico MQTT, recibe los datos y los muestra en una tabla dinámica.
-   `Dockerfile`: Define la imagen Docker para ambos servicios.
-   `docker-compose.yml`: Orquesta la ejecución de los contenedores del dispositivo y del servicio en la nube.
-   `requirements.txt`: Lista las dependencias de Python (`paho-mqtt`, `rich`).