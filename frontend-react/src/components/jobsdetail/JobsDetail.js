import React, { useState, useEffect } from 'react';
import './JobsDetail.css';
import { useForm } from 'react-hook-form';

function JobsDetail({ match }) {

  useEffect(() => {
    fetchJob();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const fetchJob = async () => {
    const data = await fetch(`http://localhost:5001/jobs/${match.params.id}`);
    const job = await data.json();
    setJob(job)
  }

  const [job, setJob] = useState({});

  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => {
    const formData = new FormData();
    formData.append("resume", data.resume[0]);
    console.log(data.resume[0])
  }
  return (
    <div className='detail-job-wrapper'>
      <h3 className='detail-job-title'>{job.title}</h3>
      <p className='detail-job-company-date'>Posted {job.created} by {job.company}</p>
      <div className='detail-job-loc-sal-wrapper'>
        <p><strong>Salary: {job.salary} per annum</strong></p>
        <p><strong>Location: {job.location}</strong></p>
      </div>
      <div className='detail-job-desc-wrapper'>
        <p>{job.description}</p>
      </div>
      <div className='detail-job-upload'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="file"  {...register('resume')} />
          <button className='detail-job-apply-btn'>Apply</button>
        </form>
      </div>
    </div>
  );
}

export default JobsDetail;