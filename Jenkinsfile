pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-ci-cd-app"
        CONTAINER_NAME = "flask-app"
        PORT = "5000"
    }

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/Ashutosh-9216/flask-ci-cd-app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove existing container if it exists
                    sh """
                    if [ \$(docker ps -aq -f name=$CONTAINER_NAME) ]; then
                        docker stop $CONTAINER_NAME || true
                        docker rm $CONTAINER_NAME || true
                    fi
                    docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME
                    """
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed! Check the logs above for details."
        }
        success {
            echo "Build and deployment completed successfully."
        }
    }
}

