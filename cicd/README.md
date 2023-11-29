# Deploy Proxy Application

This GitHub Actions workflow automates the build, test and deployment to a server. The workflow consists of two jobs: `build` and `deploy`. 


## **IMPORTANT** 

Adjust the `your-image-name:tag` & `Container Name` and port mappings (`-p`) based on the application.
This pipeline assumes that the Docker image contains the necessary configurations for your proxy application, and it exposes the application on port 8080. Adjust the Docker-related commands and configurations based on your specific requirements.


The pipeline is triggered on each push to the main branch and performs the following tasks:

## Build Job

- **Checkout Repository:** Checks out the repository using the `actions/checkout` action.

- **Set up Node.js:** Configures the environment with Node.js version 14 using the `actions/setup-node` action.

- **Install Dependencies:** Installs project dependencies using `npm install`.

- **Run Tests:** Executes tests for the application using `npm test`.

- **Build Docker Image:** Builds a Docker image for the application using the Dockerfile in the repository.

- **Log in to Docker Hub:** Logs in to Docker Hub using the provided Docker Hub username and password stored as secrets.

- **Push Docker Image to Docker Hub:** Pushes the built Docker image to Docker Hub, tagging it as `latest`.

## Deploy Job

The `deploy` job is dependent on the successful completion of the `build` job and is triggered automatically. It deploys the application to a server using SSH:

- **Install SSH key:** Installs the SSH private key for authentication.

- **SSH into the Server and Deploy:**
  - Uses SSH to connect to the specified server IP address as the user.
  - Stops and removes the existing Docker container (if any).
  - Pulls the latest Docker image from Docker Hub.
  - Runs a new Docker container, exposing it on port 8080.

### Secrets

Make sure to set the following secrets in your GitHub repository:

- **DOCKERHUB_USERNAME:** Your Docker Hub username.
- **DOCKERHUB_PASSWORD:** Your Docker Hub password.
- **SSH_PRIVATE_KEY:** The private SSH key for authenticating with the deployment server.

### Server Configuration

Replace the placeholder values in the SSH commands with your actual server details:

- **user:** The username to use when connecting to the server.
- **your-server-ip-address:** The IP address of your deployment server.

### Docker Container Configuration

Replace the placeholder values in the Docker commands with your actual container details:

- **your-container-name:** The name to assign to the running container.
- **your-dockerhub-username:** Your Docker Hub username.
- **your-image-name:** The name of the Docker image.

