import React from 'react';
import './JobsDetail.css';
import { useForm } from 'react-hook-form';

function JobsDetail({ match }) {
  const job = [
    {
      id: 1,
      jobtitle: "Corporate manager",
      salary: "£40,000",
      date: "11/12/1963",
      location: "London",
      company: "Tesla",
      sector: "Business Management",
      jobdescription: "long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less"
    }
  ]

  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => {
    const formData = new FormData();
    formData.append("resume", data.resume[0]);
    console.log(data.resume[0])
  }
  return (
    <div className='detail-job-wrapper'>
      <h3 className='detail-job-title'>{job[0].jobtitle}</h3>
      <p className='detail-job-company-date'>Posted {job[0].date} by {job[0].company}</p>
      <div className='detail-job-loc-sal-wrapper'>
        <p><strong>Salary: {job[0].salary} per annum</strong></p>
        <p><strong>Location: {job[0].location}</strong></p>
      </div>
      <div className='detail-job-desc-wrapper'>
        <p>{job[0].jobdescription}</p>
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