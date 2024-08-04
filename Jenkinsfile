pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                script {
                    sh '''
                    #!/bin/bash

                    # Actualiza los paquetes e instala las dependencias necesarias
                    sudo apt update
                    sudo apt install -y wget gnupg python3-pip git

                    # Instala la última versión de Python 3 (si no está instalada)
                    sudo apt install -y python3

                    # Agrega el repositorio de Google Chrome y la clave pública
                    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
                    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee -a /etc/apt/sources.list.d/google-chrome.list

                    # Actualiza los repositorios e instala Google Chrome
                    sudo apt update
                    sudo apt install -y google-chrome-stable

                    # Clona el repositorio (si no está ya clonado)
                    if [ ! -d "PythonAllureSelenium-v1.3" ]; then
                      git clone https://github.com/performanceDemon/PythonAllureSelenium-v1.3
                    fi

                    cd PythonAllureSelenium-v1.3

                    # Crear un entorno virtual para las dependencias de Python
                    python3 -m venv venv
                    source venv/bin/activate

                    # Instala las dependencias del proyecto
                    pip install -r requirements.txt

                    # Instala Allure si no está instalado
                    if ! command -v allure &> /dev/null; then
                        sudo apt-add-repository ppa:qameta/allure
                        sudo apt update
                        sudo apt install allure
                    fi

                    # Ejecuta las pruebas con pytest
                    source venv/bin/activate
                    pytest --alluredir=allure-results

                    # Genera el reporte de Allure
                    allure generate allure-results --clean -o allure-report

                    # Abre el reporte de Allure en un navegador
                    allure serve allure-results

                    # Desactiva el entorno virtual
                    deactivate
                    '''
                }
            }
        }
    }
}
