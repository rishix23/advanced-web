import React from 'react';
import './Postjob.css'
import { useAuth } from "../../context/auth";

function PostJob() {
  const { authTokens } = useAuth();

  return (
    <div>
      <h1>{JSON.stringify(authTokens, null, 2)}</h1>
    </div>
  );
}

export default PostJob;