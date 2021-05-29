import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import './Signup.css';
import { useAuth } from '../../context/auth';
import { Redirect } from 'react-router-dom';

function Signup() {
	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm();
	const { authTokens, setAuthTokens } = useAuth();
	const [isError, setError] = useState();

	const onSubmit = formData => {
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(formData),
		};
		fetch('http://localhost:5005/', requestOptions)
			.then(response => response.json())
			.then(data => handleResponse(data));
	};

	if (authTokens) {
		return <Redirect to="/" />;
	}

	const handleResponse = (dataReceived) => {
		if ("id" in dataReceived) {
			setAuthTokens(dataReceived.id);
		} else {
			setError(dataReceived.Message);
		}
	};



	return (
		<div className='signup-main-wrapper'>
			<h3 className='signup-title'>Signup</h3>
			<div className='signup-wrapper'>
				<form onSubmit={handleSubmit(onSubmit)}>
					<input
						type='text'
						placeholder='First name'
						{...register('firstName', {
							required: 'This is required!',
						})}
					/>
					{errors.firstName && <p>{errors.firstName.message}</p>}
					<input
						type='text'
						placeholder='Last name'
						{...register('lastName', {
							required: 'This is required!',
						})}
					/>
					{errors.lastName && <p>{errors.lastName.message}</p>}
					<input
						type='text'
						placeholder='Email'
						{...register('email', {
							required: 'This is required!',
						})}
					/>
					{errors.email && <p>{errors.email.message}</p>}
					<input
						type='password'
						placeholder='Password'
						{...register('password', {
							required: 'This is required!',
							minLength: {
								value: 8,
								message: '8 or more characters',
							},
						})}
					/>
					{errors.password && <p>{errors.password.message}</p>}
					<input type='submit' />
				</form>
				{authTokens && <h4 className='signup-msg'>Signup Success!</h4>}
				{isError && <h4 className='error-msg'>{isError}</h4>}
			</div>
		</div>
	);
}

export default Signup;
