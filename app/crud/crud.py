from fastapi import HTTPException
from bson import ObjectId
from odmantic import ObjectId as ODMObjectId
from app.database.database import engine
from app.models.models import Task, datetime

# Retrieves a specific task from the database by its ID.
#
# Args:
#   task_id (str): The unique identifier of the task to retrieve.
#
# Returns:
#   Task: The task object corresponding to the provided ID, or raises an HTTPException if no task is found.
async def get_task(task_id: str):
    try:
        task = await engine.find_one(Task, Task.id == ODMObjectId(task_id))
        if task:
            return task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving task: {str(e)}")

# Retrieves a list of tasks from the database with pagination support.
#
# Args:
#   skip (int, optional): The number of tasks to skip for pagination. Defaults to 0.
#   limit (int, optional): The maximum number of tasks to retrieve. Defaults to 100.
#
# Returns:
#   list: A list of task objects, potentially limited and offset based on the provided parameters.
async def get_tasks(skip: int = 0, limit: int = 100):
    try:
        tasks = await engine.find(Task, skip=skip, limit=limit)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving tasks: {str(e)}")

# Creates a new task in the database.
#
# Args:
#   task_data (Task): The task data to be added to the database.
#
# Returns:
#   Task: The newly created task object, including its ID and other database-managed attributes.
async def create_task(task_data: Task):
    try:
        new_task = await engine.save(task_data)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")

# Updates an existing task in the database with new data.
#
# Args:
#   task_id (str): The ID of the task to update.
#   task_data (dict): A dictionary with the updated task data.
#
# Returns:
#   Task: The updated task object, or raises an HTTPException if no task was found to update.
async def update_task(task_id: str, task_data: dict):
    try:
        task = await get_task(task_id)
        for key, value in task_data.items():
            setattr(task, key, value)
        task.updated_at = datetime.utcnow()
        await engine.save(task)
        return task
    except HTTPException:
        raise  # Re-raise the 404 error if no task is found
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating task: {str(e)}")

# Deletes a specific task from the database.
#
# Args:
#   task_id (str): The ID of the task to delete.
#
# Returns:
#   Task: The deleted task object, or raises an HTTPException if no task was found to delete.
async def delete_task(task_id: str):
    try:
        task = await get_task(task_id)
        await engine.delete(task)
        return task
    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task: {str(e)}")
