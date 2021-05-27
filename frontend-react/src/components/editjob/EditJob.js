import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import './EditJob.css'

function EditJob({ match }) {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [isJobEdited, setJobEdited] = useState(false);

  const onSubmit = (data) => {
    data.jobId = match.params.id
    console.log("dsdfsdsfldflfdsllsdldsf000", data);
    setJobEdited(true);
  }

  return (
    <div className='editjob-main-wrapper'>
      <h3 className='editjob-title'>Edit job</h3>
      <div className='editjob-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" placeholder="Job title" {...register('jobtitle', { required: "This is required!" })} />
          {errors.jobtitle && <p>{errors.jobtitle.message}</p>}
          <input type="text" placeholder="Salary" {...register('salary', { required: "This is required!" })} />
          {errors.salary && <p>{errors.salary.message}</p>}
          <input type="text" placeholder="Location" {...register('location', { required: "This is required!" })} />
          {errors.location && <p>{errors.location.message}</p>}
          <input type="text" placeholder="Your company" {...register('company', { required: "This is required!" })} />
          {errors.company && <p>{errors.company.message}</p>}
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
        {isJobEdited && <h4 className='editjob-msg'>Your job has been successfully edited!</h4>}
      </div>
    </div>
  );
}

export default EditJob;