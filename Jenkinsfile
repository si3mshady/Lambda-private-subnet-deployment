pipeline {
    agent any

    stages {
        stage('download ansible & aws cli') {
            steps {
                sh 'sudo apt install ansible -y'
                sh '''curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"
                        unzip awscliv2.zip
                        sudo ./aws/install '''
            }
        }
        stage('Test') {
            steps {
                echo 'ansible-playbook launch_pub_priv_vpc_nat.yml'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}