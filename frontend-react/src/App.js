import React, { useState } from 'react';
import './App.css';
import Nav from './components/nav/Nav';
import Home from './components/home/Home';
import Jobs from './components/jobs/Jobs';
import Signup from './components/signup/Signup';
import Login from './components/login/Login';
import Createcv from './components/createcv/Createcv';
import Footer from './components/footer/Footer';
import Postjob from './components/postjob/Postjob';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import PrivateRoute from './PrivateRoute';
import { AuthContext } from './context/auth';


function App() {
  const [authTokens, setAuthTokens] = useState();
  const setTokens = (data) => {
    localStorage.setItem("tokens", JSON.stringify(data));
  }
  return (
    <Router>
      <div className="App">
        <AuthContext.Provider value={{ authTokens, setAuthTokens }}>
          <Nav />
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/jobs" component={Jobs} />
            <Route path="/createcv" component={Createcv} />
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <PrivateRoute path="/postjob" component={Postjob} />
          </Switch>
        </AuthContext.Provider>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
