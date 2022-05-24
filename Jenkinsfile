pipeline {
    agent any
    environment{
        MY_FILE = fileExists 'py_aws'
    }
    stages{
        stage("Empty if Exist"){
             when { expression { MY_FILE == 'true' } }
            steps {
                echo MY_FILE
                sh 'sudo rmdir py_aws'
            }
        }
        stage("clone"){
            steps{
                sh 'git clone https://github.com/nikunj436/py_aws'
            }
        }

        stage("Docker Build & Push & Remove image local repo"){
            steps{
                withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'PASSWORD')]) {
                             sh 'docker login -u rabadiyanikunj436 -p $PASSWORD'
                     }
                sh 'docker build -t rabadiyanikunj436/py_aws:v1 .'    
                sh 'docker push rabadiyanikunj436/py_aws:v1 '
                sh 'docker rmi rabadiyanikunj436/py_aws:v1'
                }
        }
        stage("Deployment"){
            steps{
                sh '/var/lib/jenkins/bin/kubectl apply -f k8s'
                }
            }
        
    }
}