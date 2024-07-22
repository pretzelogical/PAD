import React from 'react';
import Navbar from './components/Navbar';
import './styles/tailwind.css';

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <div id="content" className="content ml-16 p-5 transition-all duration-500">
        <h1 className="text-3xl mb-4">Welcome to the website</h1>
        <p>This is a basic example of a vertical navigation bar that expands and collapses.</p>
      </div>
      {/* Other components like Header, Footer, SearchBar, etc. */}
    </div>
  );
};

export default App;
