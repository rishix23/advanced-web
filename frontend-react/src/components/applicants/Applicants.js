import React, { useState, useEffect } from 'react';
import './Applicants.css';
import { APPLICATION_URL } from '../../constants';

function Applicants({ match }) {
	useEffect(() => {
		fetchApplicants();
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, []);

	const fetchApplicants = async () => {
		const data = await fetch(
			`${APPLICATION_URL}/?jobId=${match.params.id}`
		);
		const applicants = await data.json();
		setApplicants(applicants);
	};

	const downloadCv = applicantid => {
		const requestOptions = {
			method: 'POST',
			responseType: 'blob',
		};
		fetch(`${APPLICATION_URL}/${applicantid}`, requestOptions).then(
			response => {
				response.blob().then(blob => {
					let url = URL.createObjectURL(blob);
					//Open the URL on new Window
					window.open(url);
				});
			}
		);
	};

	const [applicants, setApplicants] = useState([]);

	return (
		<div className='applicants-wrapper-main'>
			<h1 className='applicants-title'>Applicants</h1>
			<div className='grid-wrapper'>
				<table>
					<thead>
						<tr>
							<th>Applicant</th>
							<th>Full name</th>
							<th>Email</th>
							<th>Phone</th>
							<th>CV</th>
						</tr>
					</thead>
					<tbody>
						{applicants.map((applicant, index) => (
							<tr key={applicant.id}>
								<td>{index + 1}</td>
								<td>{applicant.full_name}</td>
								<td>{applicant.email}</td>
								<td>{applicant.phone}</td>
								<td>
									<button
										onClick={() =>
											downloadCv(applicant.id)
										}>
										Download
									</button>
								</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>
		</div>
	);
}

export default Applicants;
