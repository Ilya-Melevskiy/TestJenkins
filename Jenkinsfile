pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                // Оборачиваем шаги в withCredentials, чтобы получить путь к .env
                withCredentials([file(credentialsId: 'env-test-jenkins', variable: 'ENV_FILE')]) {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        
                        :: Загружаем переменные из .env в текущую сессию
                        for /f "usebackq tokens=*" %%a in ("%ENV_FILE%") do set %%a
                        
                        :: Теперь pytest видит BASE_URL и другие переменные
                        pytest --alluredir=./allure-results --clean-alluredir --junitxml=results.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
        }
    }
}