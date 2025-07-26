pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Ashutosh-9216/flask-ci-cd-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("flask-ci-cd-app:latest")
                }
            }
        }
        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@99.79.37.166 << EOF
                        docker stop \$(docker ps -q) || true
                        docker rm \$(docker ps -a -q) || true
                        cd flask-ci-cd-app || git clone https://github.com/Ashutosh-9216/flask-ci-cd-app.git
                        cd flask-ci-cd-app
                        git pull
                        docker build -t flask-ci-cd-app .
                        docker run -d -p 80:5000 flask-ci-cd-app
                        EOF
                    """
                }
            }
        }
    }
}

