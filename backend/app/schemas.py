from pydantic import BaseModel
from typing import List, Optional

class TeacherBase(BaseModel):
    name: str
    department_id: int

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    code: str
    name: str
    department_id: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    is_admin: bool = False

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rating: float
    comment: str
    teacher_id: int
    course_id: int
    user_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True 