# Define the Docker Compose file
COMPOSE_FILE = docker-compose.yml

# Target to start the MongoDB container manually (if needed)
.PHONY: run-mongo
run-mongo:
	@echo "Starting MongoDB container"
	-docker run -d \
		--name mongodb \
		-e ALLOW_EMPTY_PASSWORD=yes \
		-v mongodata:/data/db \
		-p 27017:27017 \
		bitnami/mongodb:latest

# Target to start the FastAPI application
.PHONY: run-api-fastapi
run-api-fastapi:
	@echo "Starting FastAPI application"
	cd app && \
		MONGO_URL="mongodb://localhost:27017" uvicorn main:app --host 0.0.0.0 --port 8000

# Target to build the Docker Compose services
.PHONY: compose-build
compose-build:
	docker compose -f $(COMPOSE_FILE) build

# Target to bring up the services defined in the Docker Compose file
.PHONY: compose-up
compose-up:
	docker compose -f $(COMPOSE_FILE) up -d

# Target to bring up and rebuild the services defined in the Docker Compose file
.PHONY: compose-up-build
compose-up-build:
	docker compose -f $(COMPOSE_FILE) up --build -d

# Target to bring down the services defined in the Docker Compose file
.PHONY: compose-down
compose-down:
	docker compose -f $(COMPOSE_FILE) down
