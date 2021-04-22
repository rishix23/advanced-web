import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import './Signup.css';


function Signup() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [isSignupSuccess, setSignupSuccess] = useState(false);

  const onSubmit = (data) => {
    console.log(data)
    setSignupSuccess(true);
  }

  return (
    <div className='signup-main-wrapper'>
      <h3 className='signup-title'>Signup</h3>
      <div className='signup-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" placeholder="First name" {...register('firstname', { required: "This is required!" })} />
          {errors.firstname && <p>{errors.firstname.message}</p>}
          <input type="text" placeholder="Last name" {...register('lastname', { required: "This is required!" })} />
          {errors.lastname && <p>{errors.lastname.message}</p>}
          <input type="text" placeholder="Email" {...register('email', { required: "This is required!" })} />
          {errors.email && <p>{errors.email.message}</p>}
          <input type="password" placeholder="Password" {...register('password', { required: "This is required!", minLength: { value: 8, message: "8 or more characters" } })} />
          {errors.password && <p>{errors.password.message}</p>}
          <input type="submit" />
        </form>
        <h4 className='signup-msg'>{isSignupSuccess && "Signup Success!"}</h4>
      </div>
    </div>
  );
}

export default Signup;