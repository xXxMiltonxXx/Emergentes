# Usa una imagen base de Python
FROM python:3.9-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de la aplicación
COPY d2d_simulation.py .

# Comando para ejecutar la simulación
CMD ["python", "d2d_simulation.py"]