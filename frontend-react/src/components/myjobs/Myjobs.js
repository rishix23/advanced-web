import React, { useState, useEffect } from 'react';
import './Myjobs.css'
import { useAuth } from "../../context/auth";
import { Link } from 'react-router-dom';
import editicon from "../../images/editicon.png";
import deleteicon from "../../images/deleteicon.png";

function Myjobs() {

  useEffect(() => {
    fetchUserJobs();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const { authTokens } = useAuth();

  const fetchUserJobs = async () => {
    const data = await fetch(`http://localhost:5000/?employerId=${authTokens}`);
    const userJobs = await data.json();
    setUserJobs(userJobs);
  }

  const deleteJob = (jobId) => {
    fetch(`http://localhost:5000/${jobId}`, { method: 'DELETE' })
      .then(() => setDeleteSuccess(true));
  }

  const [userJobs, setUserJobs] = useState([]);
  const [deleteSuccess, setDeleteSuccess] = useState(false);

  return (
    <div className='myjobs-wrapper-main'>
      <h1 className='myjobs-title'>{userJobs.length} Active job(s)</h1>
      {deleteSuccess && <h4 className='delete-msg'>Job successfully deleted!</h4>}
      <div className='myjobs-wrapper'>
        {userJobs.map(job => (
          <div key={job.id} className='myjobs-individual-info'>
            <div className='myjobs-individual-applicants'>
              <p className='myjobs-individual-title'>{job.title}</p>
              <div className='myjobs-individual-applicants-wrapper'>
                <strong><Link className="applicants-link" to={`/myjobs/applicants/${job.id}`}>View all applicants</Link></strong>
                <Link to={`/myjobs/${job.id}/edit`}>
                  <img src={editicon} alt="" />
                </Link>
                <button className="myjobs-individual-applicants-icons-button" onClick={() => deleteJob(job.id)}><img src={deleteicon} alt="" /></button>
              </div>
            </div>
            <p>Date posted: {job.created}</p>
            <p>Location: {job.location}</p>
            <p>Start date: {job.start_date}</p>
            <p>Salary: {job.salary}</p>
            <p className='myjobs-individual-description-title'>Description:</p>
            <p className='myjobs-individual-description'>{job.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Myjobs;