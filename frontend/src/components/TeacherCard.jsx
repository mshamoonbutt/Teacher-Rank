import React from 'react';
import { Link } from 'react-router-dom';

function TeacherCard({ teacher }) {
  return (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">{teacher.name}</h5>
        <h6 className="card-subtitle mb-2 text-muted">{teacher.department}</h6>
        <div className="d-flex align-items-center mb-2">
          <div className="text-warning">
            {'★'.repeat(Math.round(teacher.rating))}
            {'☆'.repeat(5 - Math.round(teacher.rating))}
          </div>
          <span className="ms-2">{teacher.rating.toFixed(1)}</span>
        </div>
        <p className="card-text">{teacher.courses.join(', ')}</p>
        <Link to={`/teachers/${teacher.id}`} className="btn btn-primary">View Details</Link>
      </div>
    </div>
  );
}

export default TeacherCard; 