pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'App Build'
        sh '''sonar-scanner \\
  -Dsonar.projectKey=easy-school \\
  -Dsonar.sources=. \\
  -Dsonar.host.url=http://184.73.117.47:9000 \\
  -Dsonar.token=sqp_0f9c6791d78b7063588acc8e88df49cce889a936
'''
      }
    }

  }
}