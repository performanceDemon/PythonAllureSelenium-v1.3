# Usar Ubuntu como imagen base
FROM ubuntu:20.04

# Establecer el entorno no interactivo para evitar preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar y instalar dependencias
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Agregar el repositorio de Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.10 python3.10-distutils

# Configurar Python 3.10 como la versión predeterminada
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Instalar pip para Python 3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# Descargar e instalar Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Configurar variables de entorno
ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROME_PATH=/usr/bin/google-chrome

# Copiar el código de la aplicación al contenedor
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias de Python desde requirements.txt
RUN pip3.10 install --no-cache-dir -r requirements.txt

# Instalar pytest y allure-pytest
RUN pip3.10 install pytest allure-pytest

# Crear el directorio para los resultados de Allure
RUN mkdir -p /app/allure-results && chmod -R 777 /app/allure-results

# Comando predeterminado para ejecutar todos los tests con pytest y generar reportes con Allure
CMD ["bash", "-c", "pytest --alluredir=/app/allure-results && allure serve /app/allure-results"]
