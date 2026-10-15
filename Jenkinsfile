pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.12'
        PROJECT_NAME = 'qa-blog-website-otomasyon'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    python --version
                    pip install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running Selenium tests...'
                bat '''
                    if not exist allure-results mkdir allure-results
                    pytest tests/ --alluredir=allure-results --html=report.html --self-contained-html -v
                '''
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure test report...'
                bat 'allure generate allure-results --clean -o allure-report'
            }
            post {
                always {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Archiving test artifacts...'
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
                archiveArtifacts artifacts: 'allure-report/**/*', allowEmptyArchive: true
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
            cleanWs()
        }
        success {
            echo 'All tests passed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
