pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh './$VENV_DIR/bin/pytest'
            }
        }
        stage('Run App') {
            steps {
                // Run app.py and save output to a file
                sh './$VENV_DIR/bin/python app.py > output.log'
            }
        }
        stage('Read Output') {
            steps {
                // Read the output.log file and display its contents
                script {
                    def output = readFile('output.log').trim()
                    echo "Output from app.py: ${output}"
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
