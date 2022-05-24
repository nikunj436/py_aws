pipeline {
    agent any
    stages{
        stage("clone"){
            steps{
                sh 'git clone https://github.com/nikunj436/py_aws'
            }
        }

        stage("Docker Build $ Push"){
            steps{
                withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'PASSWORD')]) {
                             sh 'docker login -u rabadiyanikunj436 -p $PASSWORD'
                     }
                sh 'docker build -t rabadiyanikunj436/py_aws:v1 .'    
                sh 'docker push rabadiyanikunj436/py_aws:v1 '
            }
        
        stage("Deployment")
            steps{
                sh 'kubectl apply -f k8s'
            }
            }
        }
    }
}