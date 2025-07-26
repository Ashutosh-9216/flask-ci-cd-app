pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Ashutosh-9216/flask-ci-cd-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-ci-cd-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d --name flask-app -p 5000:5000 flask-ci-cd-app
                '''
            }
        }
    }
}

