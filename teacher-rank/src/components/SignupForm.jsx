// src/components/SignupForm.js

import './SignupForm.css';

const SignupForm = () => {
  return (
    <div className="signup-form-container">
      <div className="error-message">
        <p>Error</p>
        <p>User already exists</p>
        <button className="retry-button">Try again</button>
      </div>
      
      <h1 className="signup-title">SIGN UP</h1>
      
      <div className="signup-box">
        <label>Email(FCCU)</label>
        <input type="email" placeholder="Value" />

        <label>Semester</label>
        <input type="text" placeholder="Value" />

        <label>Major</label>
        <input type="text" placeholder="Value" />

        <label>Screenshot of Transcript</label>
        <textarea placeholder="Value"></textarea>

        <button className="submit-button">Submit</button>
      </div>
    </div>
  );
};

export default SignupForm;
