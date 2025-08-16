from fastapi import APIRouter, HTTPException
from .database import db
from .models import Employee
from bson import ObjectId

router = APIRouter()

# Reference the employees collection
collection = db["employee"]

 # Serializer to convert MongoDB ObjectId into string
def employee_serializer(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "department": item["department"],
        "position": item["position"],
        "email": item["email"]
    }

@router.get("/employees")
async def read_employee():
    employees = []
    async for employee in collection.find():
        employees.append(employee_serializer(employee))
    return employees
