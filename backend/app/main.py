from fastapi import FastAPI
from .routers import teachers, courses, departments, users, reviews, auth

app = FastAPI(title="Teacher Rank")

app.include_router(teachers.router, prefix="/api", tags=["teachers"])
app.include_router(courses.router, prefix="/api", tags=["courses"])
app.include_router(departments.router, prefix="/api", tags=["departments"])
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(reviews.router, prefix="/api", tags=["reviews"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Teacher Rank API!"} 