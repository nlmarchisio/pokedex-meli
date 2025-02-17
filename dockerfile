# Usar una imagen base ligera de Python para reducir tamaño
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar solo los archivos necesarios antes de instalar dependencias
COPY requirements.txt .

# Instalar dependencias de manera eficiente
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación después de instalar dependencias (mejora caching)
COPY . .

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Usar Gunicorn para producción en lugar de ejecutar directamente Flask
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
