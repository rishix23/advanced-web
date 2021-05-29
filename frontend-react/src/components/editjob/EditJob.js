import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import './EditJob.css'

function EditJob({ match }) {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [isJobEdited, setJobEdited] = useState();

  const onSubmit = (formData) => {
    const requestOptions = {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    };
    fetch(`http://localhost:5000/${match.params.id}`, requestOptions)
      .then(response => response.json())
      .then(data => handleResponse(data));
  }

  const handleResponse = (dataReceived) => {
    if ("id" in dataReceived) {
      setJobEdited("Your job has been successfully edited!");
    } else {
      setJobEdited("Error please try again later");
    }
  };

  return (
    <div className='editjob-main-wrapper'>
      <h3 className='editjob-title'>Edit job</h3>
      <div className='editjob-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" placeholder="Job title" {...register('title')} />
          <input type="text" placeholder="Salary" {...register('salary')} />
          <input type="text" placeholder="Location" {...register('location')} />
          <input type="text" placeholder="Your company" {...register('company')} />
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
          <textarea type="text" placeholder="Job description, max 250 characters!" {...register('description', { maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.jobdescription && <p>{errors.jobdescription.message}</p>}
          <input type="submit" />
        </form>
        {isJobEdited && <h4 className='editjob-msg'>{isJobEdited}</h4>}
      </div>
    </div>
  );
}

export default EditJob;