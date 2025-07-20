# CrewAI Vue Docker Template

This template provides a minimal setup for building a CrewAI application with a Vue frontend and Docker support.

## Structure

```
crewai_vu_docker/
  backend/      # FastAPI service using CrewAI
  frontend/     # Vue 3 application
  docker-compose.yml
```

## Usage

1. Build and start the containers:

```bash
docker compose up --build
```

2. Open `http://localhost:3000` in your browser and run a query.

The frontend will send requests to the backend which uses CrewAI to generate a response.
