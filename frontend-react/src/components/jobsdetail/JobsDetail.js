import React, { useState, useEffect } from 'react';
import './JobsDetail.css';
import { useForm } from 'react-hook-form';
import { APPLICATION_URL, JOB_URL } from '../../constants';

function JobsDetail({ match }) {
	useEffect(() => {
		fetchJob();
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, []);

	const fetchJob = async () => {
		const data = await fetch(`${JOB_URL}/${match.params.id}`);
		const job = await data.json();
		setJob(job);
	};

	const [job, setJob] = useState({});
	const [isMsg, setMsg] = useState();

	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm();

	const onSubmit = data => {
		const formData = new FormData();
		formData.append('jobId', match.params.id);
		formData.append('fullname', data.fullname);
		formData.append('email', data.email);
		formData.append('phone', data.phone);
		formData.append('resume', data.resume[0]);

		const requestOptions = {
			method: 'POST',
			body: formData,
		};
		fetch(APPLICATION_URL, requestOptions)
			.then(response => response.json())
			.then(data => handleResponse(data));
	};

	const handleResponse = dataReceived => {
		if ('id' in dataReceived) {
			setMsg('Your application has been successfully submitted!');
		} else {
			setMsg(dataReceived.Message);
		}
	};

	return (
		<div className='detail-job-wrapper'>
			<h3 className='detail-job-title'>{job.title}</h3>
			<p className='detail-job-company-date'>
				Posted {job.created} by {job.company}
			</p>
			<div className='detail-job-loc-sal-wrapper'>
				<p>
					<strong>Salary: {job.salary} per annum</strong>
				</p>
				<p>
					<strong>Location: {job.location}</strong>
				</p>
			</div>
			<div className='detail-job-desc-wrapper'>
				<p>{job.description}</p>
			</div>
			<h4 className='apply-title'>Quick apply</h4>
			<div className='detail-job-upload'>
				<form onSubmit={handleSubmit(onSubmit)}>
					<input
						type='text'
						placeholder='Full name'
						{...register('fullname', {
							required: 'This is required!',
						})}
					/>
					{errors.fullname && <p>{errors.fullname.message}</p>}
					<input
						type='text'
						placeholder='Email'
						{...register('email', {
							required: 'This is required!',
						})}
					/>
					{errors.email && <p>{errors.email.message}</p>}
					<input
						type='text'
						placeholder='Contact Number'
						{...register('phone', {
							required: 'This is required!',
						})}
					/>
					{errors.phone && <p>{errors.phone.message}</p>}
					<p>Your CV pdf format</p>
					<input
						type='file'
						{...register('resume', {
							required: 'This is required!',
						})}
					/>
					{errors.resume && <p>{errors.resume.message}</p>}
					<button className='detail-job-apply-btn'>Apply</button>
				</form>
			</div>
			{isMsg && <h4 className='postapplication-msg'>{isMsg}</h4>}
		</div>
	);
}

export default JobsDetail;
