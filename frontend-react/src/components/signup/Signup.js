import React from 'react';
import { useForm } from 'react-hook-form';
import './Signup.css';
import { useAuth } from '../../context/auth';

function Signup() {
	const {
		register,
		handleSubmit,
		formState: { errors },
	} = useForm();
	const { authTokens, setAuthTokens } = useAuth();

	const onSubmit = formData => {
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(formData),
		};
		fetch('http://localhost:5005/', requestOptions)
			.then(response => response.json())
			.then(data => setAuthTokens(data.id));
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
					{errors.firstname && <p>{errors.firstname.message}</p>}
					<input
						type='text'
						placeholder='Last name'
						{...register('lastName', {
							required: 'This is required!',
						})}
					/>
					{errors.lastname && <p>{errors.lastname.message}</p>}
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
				<h4 className='signup-msg'>
					{authTokens && 'Signup Success!'}
				</h4>
			</div>
		</div>
	);
}

export default Signup;
