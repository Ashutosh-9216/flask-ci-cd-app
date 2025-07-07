pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Ashutosh-9216/flask-ci-cd-app.git'
            }
        }

        stage('Test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 5000:5000 --name flask-app flask-app
                '''
            }
        }
    }
}

