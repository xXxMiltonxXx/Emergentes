# Usa una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los scripts de la aplicación
COPY device_simulation.py .
COPY cloud_service.py .

# El CMD se especificará en el docker-compose.yml para cada servicio