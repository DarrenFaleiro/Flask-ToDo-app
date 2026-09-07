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
    }
}
