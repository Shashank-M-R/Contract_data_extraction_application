pipeline {
    agent any
    environment {
        DOCKER_IMAGE_BACKEND = 'your-dockerhub-username/contract-backend:latest'
        DOCKER_IMAGE_FRONTEND = 'your-dockerhub-username/contract-frontend:latest'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shashank-M-R/Contract_data_extraction_application.git'
            }
        }
        stage('Build & Start Application') {
            steps {
                sh 'echo "1234" | sudo -S docker-compose up --build'
            }
        }
        stage('Testing Backend Docker') {
            steps {
                sh 'pytest backend/tests'
            }
        }
    }
}