pipeline {
    agent any
    stages{
        stage("clone"){
            steps{
                sh 'rm -rf /var/lib/jenkins/workspace/Py_aws_pipeline/*'
                sh 'git clone https://github.com/nikunj436/py_aws'
            }
        }

        stage("Docker Build & Push & Remove image local repo"){
            steps{
                withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'PASSWORD')]) {
                             sh 'docker login -u rabadiyanikunj436 -p $PASSWORD'
                     }
                sh 'pwd'
                sh 'cp -rf py_aws/* .'
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