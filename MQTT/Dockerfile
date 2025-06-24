# Usa una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los scripts de la aplicación
COPY publisher.py .
COPY subscriber.py .

# El comando a ejecutar se especificará en docker-compose.yml