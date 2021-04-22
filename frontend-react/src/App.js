import React, { useState } from 'react';
import './App.css';
import Nav from './components/nav/Nav';
import Home from './components/home/Home';
import Jobs from './components/jobs/Jobs';
import JobsDetail from './components/jobsdetail/JobsDetail'
import Signup from './components/signup/Signup';
import Login from './components/login/Login';
import Createcv from './components/createcv/Createcv';
import Footer from './components/footer/Footer';
import Postjob from './components/postjob/Postjob';
import Myjobs from './components/myjobs/Myjobs';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import PrivateRoute from './PrivateRoute';
import { AuthContext } from './context/auth';


function App() {
  const [authTokens, setAuthTokens] = useState();

  return (
    <Router>
      <div className="App">
        <AuthContext.Provider value={{ authTokens, setAuthTokens }}>
          <Nav />
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/jobs" exact component={Jobs} />
            <Route path="/jobs/:id" component={JobsDetail} />
            <Route path="/createcv" component={Createcv} />
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <PrivateRoute path="/postjob" component={Postjob} />
            <PrivateRoute path="/myjobs" component={Myjobs} />
          </Switch>
        </AuthContext.Provider>
        <Footer />
      </div>
    </Router>
  );
}

export default App;