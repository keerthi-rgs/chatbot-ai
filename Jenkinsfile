pipeline {
    agent any

    environment {
        DEPLOY_PATH = "C:\\deployments\\chatbot-ai"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/keerthi-rgs/chatbot-ai.git'
            }
        }

        stage('Deploy') {
            steps {
                powershell '''
                    $dest = "C:\\deployments\\chatbot-ai"

                    if (!(Test-Path $dest)) {
                        New-Item -ItemType Directory -Path $dest -Force
                    }

                    Copy-Item -Path ".\\*" -Destination $dest -Recurse -Force -Exclude @(".git")

                    Write-Host "Deployment successful!"
                '''
            }
        }
    }

    post {
        success {
            echo 'App deployed successfully'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}