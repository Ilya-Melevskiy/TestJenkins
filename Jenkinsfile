pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Забираем код из репозитория...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Создаём виртуальное окружение и ставим зависимости...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Запускаем тесты Pytest...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest --alluredir=./allure-results --clean-alluredir --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            echo 'Публикуем отчёты...'
            
            // Публикация результатов JUnit (XML)
            junit 'results.xml'
            
            // Публикация отчёта Allure
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