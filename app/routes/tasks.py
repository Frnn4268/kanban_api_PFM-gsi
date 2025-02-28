from fastapi import APIRouter, HTTPException
from typing import List
from app.crud import crud
from app.models.models import Task

# FastAPI router for handling task-related API endpoints
router = APIRouter(prefix="/tasks", tags=["tasks"])

# Endpoint to retrieve a list of tasks with optional pagination
@router.get("/", response_model=List[Task])
async def read_tasks(skip: int = 0, limit: int = 100):
    """
    Retrieves a list of tasks from the database with optional pagination.
    
    Args:
        skip (int): The number of tasks to skip for pagination (default is 0).
        limit (int): The maximum number of tasks to retrieve (default is 100).
    
    Returns:
        List[Task]: A list of task objects containing task details.
    """
    return await crud.get_tasks(skip, limit)

# Endpoint to retrieve a single task by its ID
@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: str):
    """
    Retrieves a single task by its unique ID.
    
    Args:
        task_id (str): The ID of the task to retrieve.
    
    Returns:
        Task: The task object containing task details.
    
    Raises:
        HTTPException: If the task with the given ID does not exist, raises a 404 error.
    """
    task = await crud.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Endpoint to create a new task
@router.post("/", response_model=Task)
async def create_new_task(task: Task):
    """
    Creates a new task in the database.
    
    Args:
        task (Task): The task data to create.
    
    Returns:
        Task: The response containing the details of the created task.
    """
    return await crud.create_task(task)

# Endpoint to update an existing task by its ID
@router.put("/{task_id}", response_model=Task)
async def update_existing_task(task_id: str, task_data: dict):
    """
    Updates an existing task by its unique ID.
    
    Args:
        task_id (str): The ID of the task to update.
        task_data (dict): The new task data to update.
    
    Returns:
        Task: The response containing the details of the updated task.
    
    Raises:
        HTTPException: If the task with the given ID does not exist, raises a 404 error.
    """
    task = await crud.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Endpoint to delete a task by its ID
@router.delete("/{task_id}", response_model=Task)
async def delete_existing_task(task_id: str):
    """
    Deletes an existing task by its unique ID.
    
    Args:
        task_id (str): The ID of the task to delete.
    
    Returns:
        Task: The response containing the details of the deleted task.
    
    Raises:
        HTTPException: If the task with the given ID does not exist, raises a 404 error.
    """
    task = await crud.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Extra endpoint to retrieve all tasks for the Kanban board
@router.get("/kanban/all", response_model=List[Task])
async def get_all_for_kanban(skip: int = 0):
    """
    Retrieves all tasks for the Kanban board.
    
    Args:
        skip (int): The number of tasks to skip for pagination (default is 0).
    
    Returns:
        List[Task]: A list of task objects containing task details.
    """
    return await crud.get_tasks(skip)
