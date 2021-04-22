import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useAuth } from "../../context/auth";
import './Postjob.css'

function PostJob() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const { authTokens } = useAuth();
  const [isJobPosted, setJobPosted] = useState(false);

  const onSubmit = (data) => {
    const dataWithUser = { ...authTokens, ...data };
    console.log(dataWithUser);
    setJobPosted(true);
  }

  return (
    <div className='postjob-main-wrapper'>
      <h3 className='postjob-title'>Post a job</h3>
      <div className='postjob-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" placeholder="Job title" {...register('jobtitle', { required: "This is required!" })} />
          {errors.jobtitle && <p>{errors.jobtitle.message}</p>}
          <input type="text" placeholder="Salary" {...register('salary', { required: "This is required!" })} />
          {errors.salary && <p>{errors.salary.message}</p>}
          <input type="text" placeholder="Location" {...register('location', { required: "This is required!" })} />
          {errors.location && <p>{errors.location.message}</p>}
          <label>Sector</label>
          <select {...register('sector')}>
            <option>Finance</option>
            <option>Business Management</option>
            <option>Charity</option>
            <option>Creative Arts</option>
            <option>Construction</option>
            <option>Environment</option>
            <option>IT</option>
          </select>
          <textarea type="text" placeholder="Job description, max 250 characters!" {...register('jobdescription', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.jobdescription && <p>{errors.jobdescription.message}</p>}
          <input type="submit" />
        </form>
        {isJobPosted && <h4 className='postjob-msg'>Your job has been successfully posted!</h4>}
      </div>
    </div>
  );
}

export default PostJob;