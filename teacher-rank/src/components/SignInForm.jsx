// src/components/SignupForm.js

import './SignupForm.css';


const SignupForm = () => {
  return (
    <div className="signup-form-container">
      
      <h1 className="signup-title">SIGN IN</h1>
      
      <div className="signup-box">

        <label>Email(FCCU)</label>
        <input type="email" placeholder="roll-no@formanite.fccollege.edu.pk" />

        <label>Password</label>
        <input type="password" placeholder="*********" />

        <button className="submit-button">Submit</button>
      </div>
    </div>
  );
};

export default SignupForm;
