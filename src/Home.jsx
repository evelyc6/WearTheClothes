import React from 'react';
import './App.css';
import Input from './Input'


function Home() {
  return (
    <div className="background">
      <div>
        <div className = "topBanner">
            <header className = "Top">WearTHE Clothes</header>
            <header className = "appDesc">Prepare yourself.</header>
    `   </div>
        <Input />
      </div>
    </div>
  );
}

export default Home;