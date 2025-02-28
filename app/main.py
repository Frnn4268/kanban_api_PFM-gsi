from fastapi import FastAPI
from app.routes import tasks

# Initialize the FastAPI application instance
# The title of the application is set to "Kanban App API"
app = FastAPI(title="Kanban App API")

# Include the task routes in the FastAPI application
# This adds the task-related endpoints defined in the `tasks.router` to the application, making them accessible to users
app.include_router(tasks.router)
