from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FastAPI + MongoDB Demo")

app.include_router(router, prefix="/api", tags=["Employees"])

@app.get("/")
async def root():
    return {"message": "FastAPI with MongoDB is running 🚀"}
