pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'App Build'
        sh '''virtualenv venv
source venv/bin/activate
git clone https://github.com/clementerr/easy-school .'''
      }
    }

  }
}