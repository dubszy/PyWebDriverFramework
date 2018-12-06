// Dummy Jenkinsfile to get Jenkins pipeline up and running
// Will be updated once there is something to build

stage('Checkout') {
  node {
    checkout scm
  }
}

// TODO: Install PhantomJS and GhostDriver on the node that will run tests when framework tests are written
stage('Pre-build') {
    node {
        echo "Node Name: ${env.NODE_NAME}"
        echo "Branch name: ${env.BRANCH_NAME}"
        echo "Installing dependencies"
        sh 'pip install -r requirements.txt'
    }
}

stage('Build') {
    node {
        echo 'Jenkins pipeline is working!'
    }
}

stage('Test') {
    node {
        echo 'Running tests'
        sh 'py.test-3 tests'
    }
}
