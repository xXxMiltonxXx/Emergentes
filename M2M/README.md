# Simulación M2M Dockerizada

Este proyecto proporciona una simulación visual de comunicación Machine-to-Machine (M2M) utilizando Docker para un entorno aislado y reproducible. La salida se ha mejorado con la librería `rich` para una mejor visualización.

## Estructura del Proyecto

```
.
├── Dockerfile
├── docker-compose.yml
├── m2m_simulation.py
├── requirements.txt
└── README.md
```

## Requisitos

- Docker Desktop (o Docker Engine y Docker Compose) instalado en tu sistema.

## Cómo Ejecutar la Simulación

Sigue estos pasos para levantar y ejecutar la simulación M2M:

1.  **Clonar el Repositorio (si aplica) o Asegurarse de tener los Archivos:**

    Asegúrate de tener los archivos `Dockerfile`, `docker-compose.yml`, `m2m_simulation.py` y `README.md` en el mismo directorio.

2.  **Construir la Imagen Docker:**

    Abre una terminal en el directorio raíz del proyecto y ejecuta el siguiente comando para construir la imagen Docker. Esto instalará las dependencias necesarias dentro del contenedor.

    ```bash
    docker-compose build
    ```

3.  **Iniciar la Simulación:**

    Una vez que la imagen se haya construido, puedes iniciar la simulación ejecutando:

    ```bash
    docker-compose up
    ```

    Esto levantará el servicio definido en `docker-compose.yml` y ejecutará el script `m2m_simulation.py`.

4.  **Ver los Logs:**

    La salida de la simulación se mostrará en tu terminal. Para ver los logs de un contenedor específico, puedes usar:

```bash
docker logs -f m2m-simulator-device-01
```

O para el segundo dispositivo:

```bash
docker logs -f m2m-simulator-device-02
```

5.  **Detener la Simulación:**

    Para detener la simulación y limpiar los contenedores, presiona `Ctrl+C` en la terminal donde se está ejecutando `docker-compose up`. Luego, puedes eliminar los contenedores y redes con:

    ```bash
    docker-compose down
    ```

## Descripción de los Archivos

-   `Dockerfile`: Define la imagen Docker para la aplicación, especificando el entorno y las dependencias.
-   `docker-compose.yml`: Orquesta los servicios Docker, en este caso, define cómo se ejecuta la simulación M2M.
- `m2m_simulation.py`: El script Python que contiene la lógica de la simulación M2M, ahora con una salida visualmente atractiva.
- `requirements.txt`: Define las dependencias de Python, como `rich`.
-   `README.md`: Este archivo, con las instrucciones de uso.