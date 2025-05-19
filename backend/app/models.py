from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association table for many-to-many relationship between Teacher and Course
teacher_course = Table(
    "teacher_course",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="teachers")
    courses = relationship("Course", secondary=teacher_course, back_populates="teachers")
    reviews = relationship("Review", back_populates="teacher")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="courses")
    teachers = relationship("Teacher", secondary=teacher_course, back_populates="courses")
    reviews = relationship("Review", back_populates="course")

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teachers = relationship("Teacher", back_populates="department")
    courses = relationship("Course", back_populates="department")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Integer, default=0)  # 0 = False, 1 = True
    reviews = relationship("Review", back_populates="user")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float)
    comment = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    teacher = relationship("Teacher", back_populates="reviews")
    course = relationship("Course", back_populates="reviews")
    user = relationship("User", back_populates="reviews") 