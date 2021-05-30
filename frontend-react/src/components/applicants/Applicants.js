import React, { useState, useEffect } from 'react';
import './Applicants.css';

function Applicants({ match }) {

  useEffect(() => {
    fetchApplicants();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const fetchApplicants = async () => {
    const data = await fetch(`http://localhost:5003/?jobId=${match.params.id}`);
    const applicants = await data.json();
    setApplicants(applicants);
    console.log(applicants)
  };

  const downloadCv = (applicantid) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    };
    fetch(`http://localhost:5003/${applicantid}`, requestOptions)
      .then(response => response.json())
      .then(data => console.log(data));

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
            {applicants.map((applicant, index) =>
              <tr key={applicant.id}>
                <td>{index + 1}</td>
                <td>{applicant.full_name}</td>
                <td>{applicant.email}</td>
                <td>{applicant.phone}</td>
                <td><button onClick={() => downloadCv(applicant.id)}>Download</button></td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Applicants;