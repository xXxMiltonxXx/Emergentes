# Usa una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de simulación al contenedor
COPY m2m_simulation.py .

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "m2m_simulation.py"]