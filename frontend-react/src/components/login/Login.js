import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import './Login.css';
import { useAuth } from '../../context/auth';

function Login() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [isLoggedIn, setLoggedIn] = useState(false);
  const { setAuthTokens } = useAuth();

  const onSubmit = (data) => {
    console.log(data)
    setAuthTokens(1);
    setLoggedIn(true);
  }

  if (isLoggedIn) {
    return <Redirect to="/" />;
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
      </div>
    </div>
  );
}

export default Login;