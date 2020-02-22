import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import Home from './Home';
import Team from './Team';

function App() {
  return (
    <Router>
      <Switch>
        <Route strict exact path="/" component={Home}/>
      {/* </Switch>
      <Switch> */}
        <Route strict exact path="/meet-the-team" component = {Team}/>
      </Switch>
    </Router>
  );
}

export default App; 



