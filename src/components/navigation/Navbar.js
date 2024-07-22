import React, { useState } from 'react';
import './Navbar.css'; // Custom CSS for transitions

const Navbar = () => {
  const [expanded, setExpanded] = useState(false);

  const toggleNav = () => {
    setExpanded(!expanded);
  };

  return (
    <div id="navbar" className={`navbar fixed top-0 left-0 h-full bg-gray-800 flex flex-col items-center overflow-x-hidden ${expanded ? 'expanded' : 'w-16'}`}>
      <button className="toggle-btn text-white text-2xl mt-5 mb-5 focus:outline-none" onClick={toggleNav}>☰</button>
      <a href="#" className={`nav-link block text-white py-5 w-full text-center ${expanded ? 'opacity-1 visible' : 'opacity-0 invisible'}`}>Home</a>
      <a href="#" className={`nav-link block text-white py-5 w-full text-center ${expanded ? 'opacity-1 visible' : 'opacity-0 invisible'}`}>About</a>
      <a href="#" className={`nav-link block text-white py-5 w-full text-center ${expanded ? 'opacity-1 visible' : 'opacity-0 invisible'}`}>Contact</a>
    </div>
  );
};

export default Navbar;
