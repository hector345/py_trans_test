# Usa una imagen base de Python con las herramientas necesarias
FROM python:3.10-slim

# Instala ffmpeg para la conversión de video a audio
RUN apt-get update && apt-get install -y ffmpeg

# Crea un directorio de trabajo
WORKDIR /app

# Crear carpetas para entrada y salida
RUN mkdir input output

# Copia el archivo de requisitos (si usas otras librerías) y el script
COPY requirements.txt requirements.txt
COPY transcribe.py transcribe.py

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Comando para ejecutar el script que convierte y transcribe
CMD ["python", "transcribe.py"]