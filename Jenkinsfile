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

        stage('Install Dependencies & Run Tests') {
            steps {
                sh 'pip install -r backend/requirements.txt'
                sh 'pytest backend/tests/'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh 'sonar-scanner -Dsonar.projectKey=contract-extraction -Dsonar.host.url=http://your-sonarqube-url -Dsonar.login=your-sonarqube-token'
            }
        }

        stage('Build & Start Application') {
            steps {
                sh 'docker-compose up --build'
            }
        }

        stage('Push Images to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE_BACKEND'
                    sh 'docker push $DOCKER_IMAGE_FRONTEND'
                }
            }
        }

        stage('Update Manifest Repo') {
            steps {
                sh 'sh update_manifest.sh'
            }
        }
    }
}