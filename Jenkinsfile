pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/keerthi-rgs/chatbot-ai.git'
            }
        }

        stage('Install') {
            steps {
                bat '"C:\\Users\\keert\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\keert\\AppData\\Local\\Python\\bin\\python.exe" -m pytest'
            }
        }

        stage('Done') {
            steps {
                echo 'Build successful ✅'
            }
        }
    }
}