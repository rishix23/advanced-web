import React from 'react';
import './Home.css';
import employeeicon from '../../images/employeeicon.png'
import jobsearchicon from '../../images/jobsearchicon.png'

function Home() {

  return (
    <div className='main-home-wrapper'>
      <header>
        <h1>The process starts with you</h1>
        <h2><em>Look for your dream job or find your ideal candidate</em></h2>
      </header>
      <div className='info-wrapper'>
        <div className='info-job-hunter'>
          <h3>Job Hunter</h3>
          <img src={jobsearchicon} alt="" />
          <p>It is a long established fact that a reader will be distracted by the readable content of a page
             when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal
             distribution of letters, as opposed to using 'Content here, content here', making it look like
             readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as
             their default model text, and a search for 'lorem ipsum' will uncover many web sites still in
             their infancy. Various versions have evolved over the years, sometimes by accident, sometimes
             on purpose (injected humour and the like).</p>
        </div>
        <div className='info-employer'>
          <h3>Employer</h3>
          <img src={employeeicon} alt="" />
          <p>It is a long established fact that a reader will be distracted by
            the readable content of a page when looking at its layout.
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,
            as opposed to using 'Content here, content here', making it look like readable English.
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default
            model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.
            Various versions have evolved over the years,
            sometimes by accident, sometimes on purpose (injected humour and the like).</p>
        </div>
      </div>
    </div>
  );
}

export default Home;