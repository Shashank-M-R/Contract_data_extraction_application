pipeline {
    agent any
    environment {
        DOCKER_IMAGE_BACKEND = 'your-dockerhub-username/contract-backend:latest'
        DOCKER_IMAGE_FRONTEND = 'your-dockerhub-username/contract-frontend:latest'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/contract-project.git'
            }
        }
        stage('Build & Start Application') {
            steps {
                sh 'docker-compose up --build'
            }
        }
        stage('Testing Backend Docker') {
            steps {
                sh 'pytest backend/tests'
            }
        }
    }
}