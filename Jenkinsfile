def imageid
pipeline {
  when {
    branch 'master'
  }
  agent any

  environment {
    APP_NAME ="easy-school"
    DATE = sh(script: 'date "+%Y.%m.%d"', returnStdout: true).trim()
    NEXUS_URL = "172.31.42.214:5000"
    NEXUS_REPOSITORY = "nexus-docker"
    NEXUS_CREDENTIAL_ID = "nexuslogin"
  }

  stages {

    stage('Static Code Analysis') {
      steps {
        withSonarQubeEnv(installationName: 'sonarqube') {
          sh '/opt/sonar-scanner/bin/sonar-scanner'
        }
      }
    }

    stage('Build') {
      steps {
        sh 'sudo docker-compose build'
        script {
          imageid = sh(returnStdout: true, script: 'sudo docker image ls --filter \'reference=easy-school_web:latest\' --format \"{{.ID}}\"')
        }
      }
    }

    stage('Unit Test') {
      steps {
        sh 'nohup sudo docker-compose up &'
        sh 'python course/tests.py'
        sh 'python students/tests.py'
        sh 'python teachers/tests.py'
      }
    }

    stage('Release') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'nexuslogin', passwordVariable: 'PASSWD', usernameVariable: 'USER')]) {
          sh 'echo ${PASSWD} | sudo docker login -u ${USER} --password-stdin ${NEXUS_URL}'
        }
        withEnv(["DOCKERID=${imageid}"]) {
          sh 'sudo docker tag $DOCKERID ${NEXUS_URL}/jenkinsci-${APP_NAME}:${DATE}-${BUILD_ID}'
        }
        sh 'sudo docker push ${NEXUS_URL}/jenkinsci-${APP_NAME}:${DATE}-${BUILD_ID}'
      }
    }
  }
}
