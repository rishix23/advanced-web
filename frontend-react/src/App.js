
import './App.css';
import Nav from './components/nav/Nav';
import Home from './components/home/Home';
import Jobs from './components/jobs/Jobs';
import Signup from './components/signup/Signup';
import Login from './components/login/Login';
import Createcv from './components/createcv/Createcv';
import Footer from './components/footer/Footer';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/jobs" component={Jobs} />
          <Route path="/createcv" component={Createcv} />
          <Route path="/signup" component={Signup} />
          <Route path="/login" component={Login} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
