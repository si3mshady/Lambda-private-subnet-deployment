pipeline {
    agent any

    stages {

        stage('Check valid yaml syntax with linter ') {
            steps {
                sh 'yamllint ansible/launch_pub_priv_vpc_nat.yml'
            }
        }
       
        stage('run ansible playbook / deploy infra') {
            steps {
                echo 'ansible-playbook ansible/launch_pub_priv_vpc_nat.yml'
            }
        }
      
    }
}

//   sudo add-apt-repository -y ppa:adrienverge/ppa && sudo apt-get update
        //   sudo apt-get install yamllint