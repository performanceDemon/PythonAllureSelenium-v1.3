pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'sudo apt update'
                sh 'sudo apt install -y wget gnupg python3-pip git python3-venv'

                // Instalar Google Chrome
                sh '''
                    if ! command -v google-chrome &> /dev/null; then
                        wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
                        echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
                        sudo apt update
                        sudo apt install -y google-chrome-stable
                    fi
                '''
            }
        }

        stage('Instalar dependencias del proyecto') {
            steps {
                // Crear y activar el entorno virtual
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''

                // Instalar dependencias del proyecto
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                // Ejecutar las pruebas con pytest
                sh 'pytest --alluredir=allure-results'

                // Desactivar el entorno virtual
                sh 'deactivate'
            }
        }
    }
}