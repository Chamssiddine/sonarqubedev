import os
import subprocess
import webbrowser
import requests
import time
import platform

def check_docker_installation():
    try:
        subprocess.run(['docker', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("❌ Docker is not installed. Please follow the official Docker installation documentation.")
        print("🔗 https://docs.docker.com/engine/install/")

def download_and_run_docker_compose():
    try:
        subprocess.run(['docker-compose', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("❌ Docker Compose is not installed. Please install Docker Compose.")
        print("🔗 https://docs.docker.com/compose/install/")

    subprocess.run(['docker-compose', 'up', '-d'])
    print("🚀 Docker Compose started successfully.")

def wait_for_sonarqube():
    url = 'http://localhost:9000'
    print(f"⏳ Waiting for SonarQube to be accessible at {url}")
    
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("✅ SonarQube is accessible.")
            break
        except requests.exceptions.RequestException:
            print("❌ SonarQube is not yet accessible. Retrying in 5 seconds...")
            time.sleep(5)

def access_sonarqube():
    print("🔗 Please wait for SonarQube to start, then access it through http://localhost:9000")
    input("Press Enter when you are ready to continue...")
    print("👤 Username: admin")
    print("🔑 Password: admin")
    webbrowser.open('http://localhost:9000')

def create_precommit_hook(project_key, token, repo_path):
    # Create pre-commit hook script to run SonarScanner in Docker before each commit.
    sonar_scanner_docker_command = [
        'docker', 'run', '--rm',
        '-e', f'SONAR_HOST_URL=http://localhost:9000',
        '-e', f'SONAR_SCANNER_OPTS=-Dsonar.projectKey={project_key}',
        '-e', f'SONAR_LOGIN={token}',
        '-v', f'{repo_path}:/usr/src',
        'sonarsource/sonar-scanner-cli'
    ]
    
    precommit_script = f"""
#!/usr/bin/env python
import subprocess

subprocess.run({sonar_scanner_docker_command}, check=True)
"""

    # Determine the appropriate pre-commit hook file path based on the operating system
    hook_path = '.git/hooks/pre-commit'
    if platform.system() == 'Windows':
        hook_path = '.git/hooks/pre-commit.bat'
    
    with open(hook_path, 'w') as precommit_file:
        precommit_file.write(precommit_script)

    # Make the script executable on Unix-like systems
    if platform.system() != 'Windows':
        os.chmod(hook_path, 0o755)

    print("✨ Pre-commit hook created successfully.")

if __name__ == "__main__":
    check_docker_installation()
    download_and_run_docker_compose()
    wait_for_sonarqube()
    access_sonarqube()
    
    print("📚 Follow the documentation at github.com/chmassiddine/sonarqubedev to create a SonarQube project and come back to put in your project TOKEN and ID.")
    project_token = input("🔑 Enter the project token: ")
    project_id = input("🆔 Enter the project ID: ")
    repo_path = input("📁 Enter your repository path: ")

    create_precommit_hook(project_id, project_token, repo_path)
