from odmantic import Model
from typing import Optional, List
from datetime import datetime

# ODMantic model for the 'tasks' collection in MongoDB.
# This model defines the structure of the 'tasks' collection and its fields.
class Task(Model):
    title: str
    description: Optional[str] = None
    status: str = "todo"
    priority: str = "low"
    due_date: Optional[datetime] = None
    assignee_id: Optional[int] = None
    tags: List[str] = []
    comments: List[str] = []
    created_by: Optional[int] = None
    is_archived: bool = False
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
