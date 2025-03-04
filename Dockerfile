# Description: Dockerfile for FastAPI application

# Imagen base de python a utilizar
FROM python:3.12.4

# Nombre del carpeta de trabajo
WORKDIR /fastapi

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /fastapi/requirements.txt

# Instalar las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

# Copiar el contenido de la carpeta actual al contenedor
COPY . /fastapi/app

# Exponer el puerto 8000
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

# Validar información de lo anterior se puede realizar desde aca:
    #https://fastapi.tiangolo.com/deployment/docker/?h=docker#dockerfile