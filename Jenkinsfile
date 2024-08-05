pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/performanceDemon/PythonAllureSelenium-v1.3'
        REPO_DIR = 'PythonAllureSelenium-v1.3'
    }

    stages {
        stage('Clone or Update Repository') {
            steps {
                script {
                    if (fileExists(env.REPO_DIR)) {
                        dir(env.REPO_DIR) {
                            sh 'git pull origin main'
                        }
                    } else {
                        sh "git clone ${env.REPO_URL}"
                    }
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    dir(env.REPO_DIR) {
                        sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir(env.REPO_DIR) {
                        sh '''
                        . venv/bin/activate
                        pytest --alluredir=allure-results
                        deactivate
                        '''
                    }
                }
            }
        }
    }
}
