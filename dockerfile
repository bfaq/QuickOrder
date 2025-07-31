FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la app
COPY . .

# Puerto expuesto por gunicorn
EXPOSE 5000

# Ejecuta Gunicorn con factory
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
