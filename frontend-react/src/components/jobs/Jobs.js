import React, { useState, useEffect } from 'react';
import './Jobs.css';
import { Link } from 'react-router-dom';

function Jobs() {
	useEffect(() => {
		fetchJobs();
	}, []);

	const fetchJobs = async () => {
		const data = await fetch('http://localhost:5000/');
		const jobs = await data.json();
		setJobs(jobs);
	};

	const [jobs, setJobs] = useState([]);

	return (
		<div className='main-jobs-wrapper'>
			<h3 className='jobs-main-title'>{jobs.length} jobs found</h3>
			<div className='jobs-wrapper'>
				{jobs.map(job => (
					<div key={job.id} className='job'>
						<h4 className='job-title'>
							<Link to={`/jobs/${job.id}`}>{job.title}</Link>
						</h4>
						<p className='job-company-date'>
							Posted: {job.created} by {job.company}
						</p>
						<p className='job-salary'>
							Salary: <strong>{job.salary} per annum</strong>
						</p>
						<p className='job-location'>
							Location: <strong>{job.location}</strong>
						</p>
						<p className='job-description'>
							Description: {job.description}
						</p>
					</div>
				))}
			</div>
		</div>
	);
}

export default Jobs;
