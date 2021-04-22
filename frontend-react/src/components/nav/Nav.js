import React from 'react';
import './Nav.css';
import { Link } from 'react-router-dom';

function Nav() {
  return (
    <nav>
      <h3 className='nav-title'><Link to='/'>Jobsy</Link></h3>
      <div className='wrapper-links-dropdown'>
        <ul className="nav-links">
          <Link to='/jobs'>
            <li>Jobs</li>
          </Link>
          <Link to='/createcv'>
            <li>Create CV</li>
          </Link>
        </ul>
        <div className='dropdown'>
          <button className='dropbtn'>Employer</button>
          <div className='dropdown-content'>
            <Link to='/postjob'>
              <li>Post job</li>
            </Link>
            <Link to='/signup'>
              <li>Sign up</li>
            </Link>
            <Link to='/login'>
              <li>Login</li>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Nav;

