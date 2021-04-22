import React from 'react';
import './Myjobs.css'
import { useAuth } from "../../context/auth";

function Myjobs() {
  const { setAuthTokens } = useAuth();

  const logOut = () => {
    setAuthTokens();
  }
  return (
    <div>
      <h1>hi my jobs</h1>
      <button onClick={logOut}>Log out</button>
    </div>
  );
}

export default Myjobs;