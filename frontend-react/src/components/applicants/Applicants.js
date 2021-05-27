import React from 'react';
import './Applicants.css';

function Applicants({ match }) {
  return (
    <div className='applicants-wrapper-main'>
      {console.log("4867bnd", match.params.id)}
      <h1 className='applicants-title'>Applicants</h1>
      <div className='grid-wrapper'>
        <div className='grid'>
          <span>
            <strong>Applicant Id</strong>
          </span>
          <span>
            <strong>FullName</strong>
          </span>
          <span>
            <strong>Phone</strong>
          </span>
          <span>
            <strong>Email</strong>
          </span>
          <span>
            <strong>CV</strong>
          </span>
          <span>1</span>
          <span>Bill Bryson</span>
          <span>07922429723</span>
          <span>bbryson@gmail.com</span>
          <span>Download</span>
        </div>
      </div>
    </div>
  );
}

export default Applicants;