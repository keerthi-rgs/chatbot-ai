pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/your-username/chatbot-ai.git'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Run') {
            steps {
                bat 'python app.py'
            }
        }
    }
}