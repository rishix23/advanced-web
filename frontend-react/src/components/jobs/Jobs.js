import React from 'react';
import './Jobs.css'

function Jobs() {
  const alljobs = [
    {
      jobtitle: "Corporate manager",
      salary: "£40,000",
      date: "11/12/1963",
      location: "London",
      company: "Tesla",
      sector: "Business Management",
      jobdescription: "long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution"
    },
    {
      jobtitle: "Corporate manager",
      salary: "£40,000",
      date: "11/12/1963",
      location: "London",
      company: "Tesla",
      sector: "Business Management",
      jobdescription: "long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution"
    },
    {
      jobtitle: "Corporate manager",
      salary: "£40,000",
      date: "11/12/1963",
      location: "London",
      company: "Tesla",
      sector: "Business Management",
      jobdescription: "long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution"
    }
  ]
  return (
    <div className='main-jobs-wrapper'>
      <h3 className='jobs-main-title'>{alljobs.length} jobs found</h3>
      <div className='jobs-wrapper'>
        {alljobs.map(job => (
          <div className='job'>
            <h4 className='job-title'>{job.jobtitle}</h4>
            <p className='job-company-date'>Posted {job.date} by {job.company}</p>
            <p className='job-salary'>Salary <strong>{job.salary}</strong></p>
            <p className='job-location'>Location: <strong>{job.location}</strong></p>
            <p className='job-description'>Description {job.jobdescription}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Jobs;