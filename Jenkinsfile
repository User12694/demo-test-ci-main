pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    PYTHON_VERSION = '3.10'
  }

  stages {
    stage('CI') {
      when {
        anyOf {
          branch 'main'
          changeRequest target: 'main'
        }
      }
      stages {
        stage('Checkout') {
          steps {
            checkout scm
          }
        }

        stage('Set up Python') {
          steps {
            sh '''
              set -e
              if command -v python3.10 >/dev/null 2>&1; then
                python3.10 --version
              else
                echo "python3.10 is not installed on this Jenkins agent."
                echo "Please install Python 3.10 or run this pipeline in a Python 3.10 Docker agent."
                exit 1
              fi
            '''
          }
        }

        stage('Install dependencies') {
          steps {
            sh '''
              set -e
              python3.10 -m pip install --upgrade pip
              if [ -f requirements.txt ]; then
                python3.10 -m pip install -r requirements.txt
              fi
            '''
          }
        }

        stage('Lint with Ruff') {
          steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
              sh '''
                set -e
                python3.10 -m pip install ruff pytest coverage
                ruff check --output-format=github --target-version=py310 .
              '''
            }
          }
        }

        stage('Test with pytest') {
          steps {
            sh '''
              set -e
              coverage run -m pytest -v -s
            '''
          }
        }

        stage('Generate Coverage Report') {
          steps {
            sh '''
              set -e
              coverage report -m
            '''
          }
        }
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}