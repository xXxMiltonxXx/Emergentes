# Simulación de IoT con API RESTful (HTTP)

Este proyecto demuestra una arquitectura de IoT simple utilizando comunicación HTTP. Consiste en un backend de API RESTful construido con Flask (Python), un frontend de dashboard interactivo creado con Astro, y un simulador de dispositivo en Python. Todo el sistema está orquestado con Docker para un despliegue fácil y consistente.

## ✨ Características

- **API RESTful**: Un backend en Flask que expone endpoints para recibir (`POST`) y servir (`GET`) datos de sensores.
- **Frontend Moderno**: Un dashboard reactivo construido con [Astro](https://astro.build/) y [Preact](https://preactjs.com/) que visualiza los datos en tiempo real.
- **Simulador de Dispositivo**: Un script de Python que simula un dispositivo IoT enviando datos periódicamente a la API.
- **Dockerizado**: Todo el ecosistema (API, frontend, simulador) está contenedorizado y gestionado por Docker Compose para una fácil ejecución.
- **Comunicación en Red de Docker**: Los servicios se comunican entre sí a través de una red de Docker definida, utilizando los nombres de servicio como hostnames (ej. `http://api:5000`).

## 📂 Estructura del Proyecto

```
HTTP/
├── api/                  # Backend con Flask
│   ├── app.py            # Lógica de la API RESTful
│   ├── Dockerfile        # Dockerfile para la API
│   └── requirements.txt  # Dependencias de Python para la API
├── frontend/             # Frontend con Astro
│   ├── public/
│   │   └── favicon.svg
│   ├── src/
│   │   ├── components/
│   │   │   └── SensorData.jsx  # Componente Preact para datos en vivo
│   │   ├── layouts/
│   │   │   └── Layout.astro    # Layout base de las páginas
│   │   ├── pages/
│   │   │   └── index.astro     # Página principal del dashboard
│   │   └── styles/
│   │       └── global.css      # Estilos globales
│   ├── astro.config.mjs  # Configuración de Astro
│   ├── Dockerfile        # Dockerfile para el frontend
│   └── package.json      # Dependencias de Node.js
├── device_simulator.py   # Script del simulador de dispositivo
├── Dockerfile.device     # Dockerfile para el simulador
├── requirements-device.txt # Dependencias para el simulador
├── docker-compose.yml    # Orquesta todos los servicios
└── README.md             # Este archivo
```

## 🚀 Ejecución

### Prerrequisitos

- [Docker](https://www.docker.com/get-started) instalado y en ejecución.
- [Docker Compose](https://docs.docker.com/compose/install/) (generalmente incluido con Docker Desktop).

### Pasos

1. **Clonar el Repositorio (si aplica)**:
   Si este proyecto estuviera en un repositorio git, lo clonarías. Como está en tu máquina local, puedes omitir este paso.

2. **Construir y Ejecutar los Contenedores**:
   Abre una terminal en el directorio raíz del proyecto (`HTTP/`) y ejecuta el siguiente comando:

   ```bash
   docker-compose up --build
   ```

   - `docker-compose up` inicia todos los servicios definidos en `docker-compose.yml`.
   - `--build` fuerza la reconstrucción de las imágenes de Docker para asegurar que todos los cambios recientes en los `Dockerfile` o en el código fuente sean aplicados.

3. **Acceder al Dashboard**:
   Una vez que los contenedores estén en ejecución, abre tu navegador web y ve a:

   **[http://localhost:8080](http://localhost:8080)**

   Deberías ver el dashboard. Inicialmente, puede que muestre "Esperando datos...". Después de unos segundos, el `device-simulator` comenzará a enviar datos a la `api`, y el `frontend` los mostrará en la tabla.

4. **Verificar la API (Opcional)**:
   Puedes acceder directamente al endpoint de la API para ver los datos en formato JSON:

   **[http://localhost:5000/api/data](http://localhost:5000/api/data)**

### Ver Logs de los Contenedores

Si necesitas depurar o ver la salida de un servicio específico, puedes abrir otra terminal y usar los siguientes comandos:

- **Ver logs del frontend**:
  ```bash
  docker logs -f http-frontend
  ```

- **Ver logs de la API**:
  ```bash
  docker logs -f http-api
  ```

- **Ver logs del simulador de dispositivo**:
  ```bash
  docker logs -f http-device-simulator
  ```

### Detener la Simulación

Para detener todos los contenedores, presiona `Ctrl + C` en la terminal donde ejecutaste `docker-compose up`. Para eliminar los contenedores y la red, puedes ejecutar:

```bash
docker-compose down
```