import React from 'react';
import './Footer.css';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <div className='footer'>
      <h3 className='footer-title'>Jobsy</h3>
      <ul className='footer-nav-links'>
        <Link to='/jobs'>
          <li>Jobs</li>
        </Link>
        <Link to='/createcv'>
          <li>Create CV</li>
        </Link>
        <Link to='/signup'>
          <li>Sign up</li>
        </Link>
      </ul>
    </div>
  );
}

export default Footer;