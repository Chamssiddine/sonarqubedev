# Dockerfiles

**IMPORTANT**
 Adjust the `imagename:tag` and port mappings (`-p`) based the application.

Note: Ensure Docker is installed on your machine before running these commands.

## Nest.js Application

### Build for Local Development

```bash

# Build the Docker image for local development
docker build -t nestjs-app:development -f NestDockerfile .
```

### Build for Production

```bash

# Build the Docker image for production
docker build -t nestjs-app:production --target production -f  NestDockerfile . 
```

### Run the Docker Container

```bash
# Run the Docker container for production
docker run -p 8080:8080 nestjs-app:production
```

## Next.js Application

```bash

# Build the Docker image
docker build -t nextjs-app -f NextDockerfile . 
```

### Run the Docker Container

```bash
# Run the Docker container for Next.js
docker run -p 3000:3000 nextjs-app
```

## Node.js Application

```bash
# Build the Docker image
docker build -t nodejs-app -f NodeDockerfile .
```

### Run the Docker Container

```bash
# Run the Docker container for Node.js
docker run -p 8082:8082 nodejs-app
```

## React.js Application

```bash
# Build the Docker image
docker build --target=production -t reactjs-app -f ReaactDockerfile .
```

### Run the Docker Container

```bash
# Run the Docker container for React.js
docker run -p 3000:3000 reactjs-app 
```