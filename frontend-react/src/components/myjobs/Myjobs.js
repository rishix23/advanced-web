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
    console.log("dfsfsdfdsdfs", authTokens)
    const data = await fetch(`http://localhost:5001/jobs/${authTokens}`);
    const userJobs = await data.json();
    setUserJobs(userJobs)
  }

  const myFunction = () => {
    console.log("you clicked me")
  }

  //remember to change to array
  const [userJobs, setUserJobs] = useState({});

  return (
    <div className='myjobs-wrapper-main'>
      <h1 className='myjobs-title'>1 Active job(s)</h1>
      <div className='myjobs-wrapper'>
        <div className='myjobs-individual'>
          <div className='myjobs-individual-info'>
            <div className='myjobs-individual-applicants'>
              <p className='myjobs-individual-title'>{userJobs.title}</p>
              <strong><Link to={`/myjobs/${userJobs.id}`}>View all applicants</Link></strong>
            </div>
            <p className='myjobs-individual-posted'>Date posted: {userJobs.created}</p>
            <p>Location: {userJobs.location}</p>
            <p>Start date: {userJobs.start_date}</p>
            <p>Salary: {userJobs.salary}</p>
            <p className='myjobs-individual-description-title'>Description:</p>
            <p className='myjobs-individual-description'>{userJobs.description}</p>
          </div>
          <div className='myjobs-individual-options'>
            <div className='myjobs-individual-options-icons'>
              <Link to="/">
                <img src={editicon} alt="" />
              </Link>
              <button className="myjobs-individual-options-icons-button"><img src={deleteicon} alt="" onClick={myFunction} /></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Myjobs;