pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Confirm files') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo-app:jenkins-test .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker rm -f todo-jenkins-test || true'
                sh 'docker run -d --name todo-jenkins-test -p 5000:5000 todo-app:jenkins-test'
                sh 'sleep 5'
                sh 'curl localhost:5000'
            }    
        }
    }
}
