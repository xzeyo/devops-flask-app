// TW2 3.1 - Declarative Pipeline: checkout -> build image -> verify
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/xzeyo/devops-flask-app'
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t devops-flask-app:pipeline-${BUILD_NUMBER} .'
            }
        }
        stage('Verify image') {
            steps {
                sh 'docker image ls devops-flask-app | head -5'
            }
        }
    }
}
