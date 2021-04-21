import React from 'react';
import './Nav.css';
import { Link } from 'react-router-dom';

function Nav() {
  return (
    <nav>
      <h3 className='nav-title'>Jobsy</h3>
      <ul className="nav-links">
        <Link to='/jobs'>
          <li>Jobs</li>
        </Link>
        <Link to='/createcv'>
          <li>Create CV</li>
        </Link>
        <Link to='/signup'>
          <li>Sign up</li>
        </Link>
        <Link to='/login'>
          <li>Login</li>
        </Link>
        {/*<li>Post Job</li>*/}
        {/*<li>My Jobs</li>*/}
      </ul>
    </nav>
  );
}

export default Nav;

