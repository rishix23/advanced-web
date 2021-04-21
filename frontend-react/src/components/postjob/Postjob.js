import React from 'react';
import './Postjob.css'
import { useAuth } from "../../context/auth";

function PostJob() {
  const { setAuthTokens } = useAuth();

  const logOut = () => {
    setAuthTokens();
  }
  return (
    <div>
      <h1>hi</h1>
      <button onClick={logOut}>Log out</button>
    </div>
  );
}

export default PostJob;