import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { JOB_URL } from '../../constants';
import { useAuth } from '../../context/auth';
import './Postjob.css';

function PostJob() {
	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm();
	const { authTokens } = useAuth();
	const [isMsg, setMsg] = useState();

	const onSubmit = formData => {
		formData.employerId = authTokens;
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(formData),
		};
		fetch(JOB_URL, requestOptions)
			.then(response => response.json())
			.then(data => handleResponse(data));
	};

	const handleResponse = dataReceived => {
		if ('id' in dataReceived) {
			setMsg('Your job has been successfully posted!');
		} else {
			setMsg(dataReceived.Message);
		}
	};

	return (
		<div className='postjob-main-wrapper'>
			<h3 className='postjob-title'>Post a job</h3>
			<div className='postjob-wrapper'>
				<form onSubmit={handleSubmit(onSubmit)}>
					<input
						type='text'
						placeholder='Job title'
						{...register('title', {
							required: 'This is required!',
						})}
					/>
					{errors.title && <p>{errors.title.message}</p>}
					<input
						type='text'
						placeholder='Salary'
						{...register('salary', {
							required: 'This is required!',
						})}
					/>
					{errors.salary && <p>{errors.salary.message}</p>}
					<input
						type='text'
						placeholder='Location'
						{...register('location', {
							required: 'This is required!',
						})}
					/>
					{errors.location && <p>{errors.location.message}</p>}
					<input
						type='text'
						placeholder='Your company'
						{...register('company', {
							required: 'This is required!',
						})}
					/>
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
					<textarea
						type='text'
						placeholder='Job description, max 250 characters!'
						{...register('description', {
							required: 'This is required!',
							maxLength: {
								value: 250,
								message: 'Max length 250 characters!',
							},
						})}></textarea>
					{errors.description && <p>{errors.description.message}</p>}
					<input type='submit' />
				</form>
				{isMsg && <h4 className='postjob-msg'>{isMsg}</h4>}
			</div>
		</div>
	);
}

export default PostJob;
