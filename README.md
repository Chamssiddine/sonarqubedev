# SonarQubeDev Setup Script

This script automates the setup process for integrating SonarQube into your development workflow using Docker and SonarScanner. Follow the steps below to get started.

## Prerequisites

Make sure you have the following software installed on your system:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

1. Clone the repository and run the script:

    ```bash
    git clone https://github.com/Chamssiddine/sonarqubedev
    ```

    ```bash
    python3 sonarqube.py
    ```

   This script performs the following steps:

   - Checks if Docker is installed. If not, it provides a link to the [official Docker installation documentation](https://docs.docker.com/engine/install/).
   - Checks if Docker Compose is installed. If not, it provides a link to the [Docker Compose installation guide](https://docs.docker.com/compose/install/).
   - Starts Docker Compose to set up SonarQube.

2. Wait for SonarQube to become accessible:

   The script waits for SonarQube to be accessible at http://localhost:9000.

3. Access SonarQube:

   After SonarQube is accessible, the script prompts you to press Enter to continue. It then opens SonarQube in your default web browser.

   - **Username:** admin
   - **Password:** admin

4. Follow the documentation:

   The script instructs you to follow the documentation at [github.com/chmassiddine/sonarqubedev](https://github.com/chmassiddine/sonarqubedev) to create a SonarQube project. Once you have your project token and ID, enter them when prompted.

   ```bash
   🔑 Enter the project token: <your_project_token>
   🆔 Enter the project ID: <your_project_id>
   📁 Enter your repository path: <your_repository_path>
   ```

5. Create Pre-commit Hook:

   The script creates a pre-commit hook that runs SonarScanner in Docker before each commit. The hook is stored in `.git/hooks/pre-commit` for Unix-like systems and `.git/hooks/pre-commit.bat` for Windows.

   The script sets the necessary environment variables for the SonarScanner Docker command using the provided project key, token, and repository path.

   ```bash
   #!/usr/bin/env bash  # or @echo off for Windows
   
   docker run --rm \
      --network sonarqube \
      -e SONAR_HOST_URL=http://sonarqube:9000 \
      -e SONAR_SCANNER_OPTS=-Dsonar.projectKey=<your_project_key> \
      -e SONAR_LOGIN=<your_project_token> \
      -v <your_repository_path>:/usr/src \
      sonarsource/sonar-scanner-cli
   ```

   Make sure to replace `<your_project_key>`, `<your_project_token>`, and `<your_repository_path>` with your actual project key, token, and repository path.

   Now, the pre-commit hook will run SonarScanner before each commit, ensuring code quality and adherence to coding standards.