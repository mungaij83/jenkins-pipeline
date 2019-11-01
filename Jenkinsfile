pipeline {
    agent { 
        docker {
            image 'python:3.5.1'
            registryUrl 'dr.sqilab.com:25000'
            registryCredentialId ''
        }
    }
    stages {
        stage('build'){
            steps{
                sh 'python version'
            }
        }
        stage('Test'){
            steps {
                sh 'echo "Testing application"'
            }
        }
        stage('Deploy'){
            steps{
                timeout(time: 3,unit:'MINUTES'){
                    sh 'echo "Welcome to failed pipeline"'
                }
            }
        }
    }
    post {
        always{
            echo 'Clean up build'
        }
        success {
            echo 'Successful build'
        }
        failure{
            echo 'Clean failed build'
        }
    }
}