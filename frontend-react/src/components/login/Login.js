import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import './Login.css';
import { useAuth } from '../../context/auth';

function Login() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const { authTokens, setAuthTokens } = useAuth();
  const [isError, setError] = useState();

  const onSubmit = (formData) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    };
    fetch('http://localhost:5004/', requestOptions)
      .then(response => response.json())
      .then(data => handleResponse(data));
  };

  const handleResponse = (dataReceived) => {
    if ("id" in dataReceived) {
      setAuthTokens(dataReceived.id);
    } else {
      setError(dataReceived.Message);
    }
  };

  if (authTokens) {
    return <Redirect to="/myjobs" />;
  }

  return (
    <div className='login-main-wrapper'>
      <h3 className='login-title'>Login</h3>
      <div className='login-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" placeholder="Email" {...register('email', { required: "This is required!" })} />
          {errors.email && <p>{errors.email.message}</p>}
          <input type="password" placeholder="Password" {...register('password', { required: "This is required!", minLength: { value: 8, message: "8 or more characters" } })} />
          {errors.password && <p>{errors.password.message}</p>}
          <input type="submit" />
          <Link to="/signup">Don't have an account?</Link>
        </form>
        {isError && <h4 className='error-msg'>{isError}</h4>}
      </div>
    </div>
  );
}

export default Login;