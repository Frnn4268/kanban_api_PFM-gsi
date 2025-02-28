from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "todo"
    priority: Optional[str] = "low"
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None
    tags: Optional[List[str]] = []
    comments: Optional[List[str]] = []
    created_by: Optional[int] = None
    is_archived: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: str  = Field(..., alias="id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
