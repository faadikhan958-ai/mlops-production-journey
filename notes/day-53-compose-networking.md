# Day 53 — Docker Compose Lifecycle & Networking

## Objective
Understand Docker Compose lifecycle management and enable communication between containers using Docker networking and service-name DNS.

## 1. Docker Compose Lifecycle

Practiced the following commands:

| Command | Purpose |
|---|---|
| `docker compose config --quiet` | Validate Compose configuration |
| `docker compose build` | Build Docker images |
| `docker compose up -d` | Create and start containers in background |
| `docker compose ps` | Inspect running services |
| `docker compose logs -f` | Follow container logs |
| `docker compose exec` | Execute commands inside running containers |
| `docker compose stop` | Stop containers without removing them |
| `docker compose start` | Start stopped containers |
| `docker compose down` | Remove Compose containers and network |

## 2. Host vs Container Ports

The API service uses port mapping:

`8000:8000`

- First `8000`: Host port.
- Second `8000`: Container port.
- The host accesses the API through `http://127.0.0.1:8000`.

## 3. Bridge Networking

Both Compose services are connected to the same bridge network:

`mlops-network`

Docker network inspection confirmed that both containers were attached to this network.

## 4. Container Localhost

- `localhost` inside the API container refers to the API container itself.
- `localhost` inside the model_inference container refers to that container itself.

## 5. Docker DNS & Service Discovery

Docker DNS resolves service names to container IP addresses.

Tested from the API container:

`socket.gethostbyname('model_inference')`

Observed IP:

`172.18.0.3`

The IP can change when containers are recreated, so service names should be used instead of hardcoded IP addresses.

Example:

`http://model_inference:8000`

Note: This is an example address. The model_inference service currently does not run an HTTP server.

## 6. Practical Verification

- API container Python version: 3.11.18
- model_inference container Python version: 3.9.25
- Host API documentation endpoint: HTTP 200 OK
- Docker DNS resolution: Successful
- Compose configuration validation: Successful
- Both containers recreated and verified as Up.

## Key Engineering Concepts
- Container lifecycle management
- Docker bridge networking
- Host-to-container port mapping
- Container isolation
- Docker embedded DNS
- Service-name-based discovery

## Outcome
Successfully practiced Docker Compose lifecycle commands, inspected network membership, tested service-name DNS resolution, and verified host-to-container API connectivity.

## Repository
https://github.com/faadikhan958-ai/mlops-production-journey
