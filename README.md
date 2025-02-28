# Kanban API - GSI

## Overview

This project is a Kanban Task Management API built with FastAPI, Odmantic, and MongoDB. It provides CRUD operations for managing tasks and follows a structured architecture to ensure scalability and maintainability.

## Features

- Create, read, update, and delete (CRUD) tasks.

- Database schema and seed data included.

- Containerized deployment using Docker Compose.

- Preconfigured Makefile for easier command execution.

- Postman collection for testing API endpoints.

## Directory Structure

```plaintext
├── app
│   ├── crud
│   │   └── crud.py           # CRUD operations for tasks
│   ├── database
│   │   ├── database.py       # Database connection
│   │   └── schemas.py        # Pydantic models for request validation
│   ├── main.py               # FastAPI application entry point
│   ├── models
│   │   └── models.py         # SQLAlchemy database models
│   └── routes
│       └── tasks.py          # API routes for task management
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile                # Docker image definition
├── Makefile                  # Makefile for common commands
├── poetry.lock               # Poetry dependencies lock file
├── postman_collection.json   # Postman collection for API testing
├── pyproject.toml            # Project dependencies and configuration
└── README.md                 # Project documentation
```

## Services

This project consists of the following services:

| Service  | Description  | Port  |
| ------------ | ------------ | ------------ |
| FastAPI | Main application handling API requests  | 8000  |
| MongoDB  | Database service storing task data  | 27017  |

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose
- Make (optional, for simplified commands)

### Running the Application with Docker Compose

1. Clone the repository:

	```bash
	git clone https://github.com/Frnn4268/kanban_api_PFM-gsi
		 
	cd kanban_api_PFM-gsi
	```

2. Start the application:

	```bash
	docker-compose up --build
	```
	For other hand
	```bash
	docker-compose up --build -d
	```

	#### When to use:

	> - Use docker-compose up --build if you want to see logs in the terminal and ensure the containers are running.
	> -  Use docker-compose up --build -d if you prefer the containers to run in the background without keeping the terminal session open for logs.

3. The API will be available at:

	```bash
	http://localhost:8000
	```
### Running the Application with Makefile

To run the application using the ***Makefile***, you can use the following commands:

- Start MongoDB:

	```bash
	make run-mongo
	```
	
	This will start a MongoDB container with a persistent volume.

- Run the FastAPI application locally:

	```bash
	make run-api-fastapi
	```
	
	This runs the FastAPI application using uvicorn.

- Build the Docker Compose services:

	```bash
	make compose-build
	```
	
	This builds the images defined in docker-compose.yml.

- Start the entire application (recommended):

	```bash
	make compose-up-build
	```
	
	**Use this command to bring up all services, ensuring everything is built correctly.** It will start the database, initialize it with the necessary schema and seed data, and then launch the FastAPI backend.

- Stop all services:

	```bash
	make compose-down
	```
	
	This shuts down the running containers.

## API Endpoints

| Method  | Endpoint  | Description  |
| ------------ | ------------ | ------------ |
|  GET |  /tasks/  |  Retrieve all tasks  |
| GET  |  /tasks/{id}  | Retrieve a specific task by ID |
| GET  | /tasks/kanban/all | Retrieve all tasks of Kanban  |
| POST  | /tasks/  | Create a new task  |
| PUT  | /tasks/{id}  | Update an existing task  |
| DELETE  | /tasks/{id}  | Delete a task  |

## Database Requirements

- Database URL: ***MONGO_URL=mongodb://localhost:27017***

| Database name  | Password  | 
| ------------ | ------------ | 
|  none |  none  |  

## Testing with Postman Collection

To test the API, you can use:

- Postman: Import ***postman_collection.json***.
	(Collection attached to this project.)

## Contributors

- Fernando Martínez - [Github Profile](https://github.com/Frnn4268 "Github Profile")
