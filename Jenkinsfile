pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'App Build'
        sh '''cd /home/ubuntu/easy-school
docker-compose build
'''
      }
    }

  }
}