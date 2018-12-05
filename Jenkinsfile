// Dummy Jenkinsfile to get Jenkins pipeline up and running
// Will be updated once there is something to build

#!groovy

stage('Checkout') {
    checkout('scm')
}


stage('Pre-build') {
    node {
        echo "Node Name: ${env.NODE_NAME}"
        echo "Branch name: ${env.BRANCH_NAME}"
        echo "Git Commit: ${env.GIT_COMMIT}"
        echo "Git Previous Commit: ${env.GIT_PREVIOUS_COMMIT}"
        echo "Git Previous Successful Commit: ${env.GIT_PREVIOUS_SUCCESSFUL_COMMIT}"
    }
}

stage('Build') {
    node {
        echo 'Jenkins pipeline is working!'
    }
}
