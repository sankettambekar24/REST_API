pipeline {
    agent {
        label 'Ubuntu-Agent'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Django Check') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py check
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }
         stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            script {
                def scannerHome = tool 'SonarQube-Scanner'

                sh """
                    ${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=REST_API \
                    -Dsonar.projectName=REST_API \
                    -Dsonar.sources=.
                """
            }
        }
    }
}


        stage('Dependency Check') {
    steps {
        script {
            def dependencyCheckHome = tool 'Dependency-Check'

            withCredentials([
                string(
                    credentialsId: 'nvd-api-key',
                    variable: 'NVD_API_KEY'
                )
            ]) {
                sh """
                    mkdir -p dependency-check-report

                    ${dependencyCheckHome}/bin/dependency-check.sh \
                    --project 'REST_API' \
                    --scan . \
                    --format HTML \
                    --format XML \
                    --out dependency-check-report \
                    --nvdApiKey "\$NVD_API_KEY"
                """
            }
        }
    }
}
    }
}
