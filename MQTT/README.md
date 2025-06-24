# Simulación de Publicador/Suscriptor MQTT

Este proyecto demuestra un caso de uso clásico de IoT utilizando el protocolo MQTT. Consiste en dos scripts de Python:

1.  `publisher.py`: Simula un dispositivo IoT que mide temperatura y humedad y publica estos datos en un topic MQTT.
2.  `subscriber.py`: Simula una aplicación o servicio que se suscribe a dicho topic para recibir y visualizar los datos en tiempo real.

Ambos scripts utilizan un broker MQTT público (`broker.hivemq.com`) y la librería `rich` para una visualización atractiva en la terminal.

## Características

-   **Protocolo MQTT**: Comunicación ligera y eficiente, ideal para IoT.
-   **Visualización Mejorada**: Uso de la librería `rich` para mostrar paneles, tablas y logs coloreados.
-   **Independencia**: El publicador y el suscriptor son scripts independientes que pueden ejecutarse en la misma o en diferentes máquinas.
-   **Broker Público**: No requiere configuración de un broker local, facilitando la prueba.

## Estructura del Proyecto

```
.
├── Dockerfile
├── docker-compose.yml
├── publisher.py
├── subscriber.py
└── requirements.txt
```

## Cómo Ejecutar la Simulación con Docker

### 1. Requisitos Previos

-   Tener Docker y Docker Compose instalados.

### 2. Construir y Ejecutar

Abre una terminal en el directorio raíz del proyecto y ejecuta:

```bash
docker-compose up --build
```

Este comando construirá la imagen de Docker y luego iniciará los dos contenedores (`publisher` y `subscriber`).

### 3. Ver la Simulación

La salida de `docker-compose` mostrará los logs de ambos contenedores mezclados. Para una visualización más clara, es recomendable abrir **dos terminales adicionales**.

**En la Terminal 1 (Suscriptor):**

```bash
docker logs -f mqtt-subscriber
```

Verás la tabla del suscriptor actualizándose en tiempo real.

**En la Terminal 2 (Publicador):**

```bash
docker logs -f mqtt-publisher
```

Verás los mensajes que el publicador está enviando.

### 4. Detener la Simulación

Presiona `Ctrl+C` en la terminal donde ejecutaste `docker-compose up`.