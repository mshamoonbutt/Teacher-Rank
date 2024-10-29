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

        <label>Name</label>
        <input type="text" placeholder="Value" />

        <label>Email(FCCU)</label>
        <input type="email" placeholder="Value" />

        <label>Semester</label>
        <select name="semester" required>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>


        <label>Major</label>
        <select name="major" required>
          <option value="computer-science">Computer Science</option>
          <option value="business">Business</option>
          <option value="technology">Technology</option>
        </select>

        <label>Screenshot of Transcript</label>
        <textarea placeholder="Value"></textarea>

        <button className="submit-button">Submit</button>
      </div>
    </div>
  );
};

export default SignupForm;
