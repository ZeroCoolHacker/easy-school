pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'App Build'
        sh '''sudo docker-compose build
'''
      }
    }

  }
}