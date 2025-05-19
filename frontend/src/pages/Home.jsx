import React from 'react';
import TeacherCard from '../components/TeacherCard';

function Home() {
  // This will be replaced with actual API data
  const featuredTeachers = [
    {
      id: 1,
      name: "Dr. John Smith",
      department: "Computer Science",
      rating: 4.5,
      courses: ["Introduction to Programming", "Data Structures"]
    },
    {
      id: 2,
      name: "Prof. Jane Doe",
      department: "Mathematics",
      rating: 4.8,
      courses: ["Calculus", "Linear Algebra"]
    }
  ];

  return (
    <div className="container">
      <div className="row mb-4">
        <div className="col">
          <h1>Welcome to Teacher Rank</h1>
          <p className="lead">Find and rate your teachers to help others make informed decisions.</p>
        </div>
      </div>

      <div className="row mb-4">
        <div className="col">
          <h2>Featured Teachers</h2>
          <div className="row">
            {featuredTeachers.map(teacher => (
              <div key={teacher.id} className="col-md-6">
                <TeacherCard teacher={teacher} />
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h3>Find Teachers</h3>
              <p>Search for teachers by name, department, or course.</p>
              <button className="btn btn-primary">Browse Teachers</button>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h3>Explore Courses</h3>
              <p>Discover courses and see which teachers are teaching them.</p>
              <button className="btn btn-primary">Browse Courses</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home; 