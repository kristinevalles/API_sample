from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name: str
    department: str
    position: str
    email: str
    id: Optional[str] = None    # MongoDB _id will map here
