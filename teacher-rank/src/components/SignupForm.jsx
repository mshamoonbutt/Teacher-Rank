// src/components/SignupForm.js

import './SignupForm.css';

const SignupForm = () => {
  return (
    <div className="signup-form-container">
      
      <h1 className="signup-title">SIGN UP</h1>
      
      <div className="signup-box">

        <label>Name</label>
        <input type="text" placeholder="Value" />

        <label>Email(FCCU)</label>
        <input type="email" placeholder="roll-no@formanite.fccollege.edu.pk" />

        <label>Semester</label>
        <select name="semester" required>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10</option>
        </select>


        <label>Major</label>
        <select name="major" required>
          <option value="computer-science">Computer Science</option>
          <option value="business">Business</option>
          <option value="bio-Tech">Bio Tech</option>
          <option value="mass-com">Mass Com</option>
          <option value="political-science">Political Science</option>
          <option value="psychology">Psychology</option>
        </select>

        <label>Screenshot of Transcript</label>
        <textarea placeholder="Value"></textarea>

        <button className="submit-button">Submit</button>
      </div>
    </div>
  );
};

export default SignupForm;
