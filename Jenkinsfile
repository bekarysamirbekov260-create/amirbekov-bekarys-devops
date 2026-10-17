pipeline {
    agent any

    environment {
        STUDENT_NAME    = 'Bekarys'
        STUDENT_SURNAME = 'Amirbekov'
        STUDENT_GROUP   = 'IT2 2309'
        STUDENT_ID      = '37898'
        IMAGE_NAME      = 'amirbekov-bekarys-devops'
        CONTAINER_NAME  = 'amirbekov-bekarys-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
                echo "Group: ${env.STUDENT_GROUP}"
                echo "Student ID: ${env.STUDENT_ID}"
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x scripts/Amirbekov_Bekarys_system.sh'
                sh './scripts/Amirbekov_Bekarys_system.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'bash -n scripts/Amirbekov_Bekarys_system.sh'
                sh 'test -f Dockerfile'
                sh 'test -f Amirbekov_Bekarys_info.txt'
                sh 'grep -q "$STUDENT_ID" Amirbekov_Bekarys_info.txt'
                echo 'All checks passed'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest -t $IMAGE_NAME:$BUILD_NUMBER .'
                sh 'docker images | grep $IMAGE_NAME'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME \
                        -e STUDENT_NAME=$STUDENT_NAME \
                        -e STUDENT_SURNAME=$STUDENT_SURNAME \
                        -e STUDENT_GROUP="$STUDENT_GROUP" \
                        -e STUDENT_ID=$STUDENT_ID \
                        $IMAGE_NAME:latest
                    sleep 3
                    docker ps --filter name=$CONTAINER_NAME
                    docker logs $CONTAINER_NAME
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully' }
        failure { echo 'Pipeline failed - check the stage that turned red' }
    }
}
