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
    const data = await fetch(`http://localhost:5001/jobs/${JSON.parse(authTokens).userid}`);
    const userJobs = await data.json();
    console.log(userJobs)
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
            <p className='myjobs-individual-title'>{userJobs.title}</p>
            <p className='myjobs-individual-posted'>Date posted: {userJobs.created}</p>
            <p>Location: {userJobs.location}</p>
            <p>Start date: {userJobs.start_date}</p>
            <p>Salary: {userJobs.salary}</p>
            <p className='myjobs-individual-description-title'>Description:</p>
            <p className='myjobs-individual-description'>{userJobs.description}</p>
          </div>
          <div className='myjobs-individual-options'>
            <p className='myjobs-individual-options-title'>Options</p>
            <div className='myjobs-individual-options-icons'>
              <Link to="/">
                <img src={editicon} alt="" />
              </Link>
              <button className="myjobs-individual-options-icons-button"><img src={deleteicon} alt="" onClick={myFunction} /></button>
            </div>
            <Link to={`/myjobs/${userJobs.id}`}>View all applicants</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Myjobs;