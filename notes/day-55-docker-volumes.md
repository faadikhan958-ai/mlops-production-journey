
# Day 55 - Docker Volumes and Persistent Data

## Objective
Understand how to preserve data when Docker containers are removed and recreated.

## Named Volume Experiment
- Created a disposable Docker Compose service.
- Mounted named volume `lab_data` at `/app/data`.
- Created `proof.txt` inside the container.
- Removed and recreated the container.
- Verified that the file survived container recreation.

## Bind Mount Experiment
- Windows host path: `volume-lab/host-data`
- Container path: `/app/host-data`
- Verified host-to-container file access.
- Updated the host file from inside the container.
- Verified the update on Windows.
- Removed and recreated the container and confirmed the file remained.

## Down vs Down -v
- `docker compose down`: Removed containers and network; named volume survived.
- `docker compose down -v`: Removed the Compose-managed named volume.
- Verified that the Windows bind-mounted host folder remained intact.

## Project Persistence Audit
- Inspected root docker-compose.yml and FastAPI main.py.
- Current API returns predictions but does not persist prediction history.
- ML model is packaged with the application image.
- No PostgreSQL database exists yet.
- Decision: Do not add an unnecessary volume now.
- Add a named volume for PostgreSQL data during Days 57-63.

## Key Learnings
- Containers are disposable.
- Named volumes store data outside the container lifecycle.
- Bind mounts connect host directories to container paths.
- Docker-managed named volumes and host bind-mounted folders have different deletion behaviour.

## Career Sprint
Completed the Day 55 internship application/contact task and updated the tracker.

## Completion Evidence
- Named volume persistence verified.
- Bind mount two-way access verified.
- Container recreation persistence verified.
- `down` and `down -v` behaviour verified.
