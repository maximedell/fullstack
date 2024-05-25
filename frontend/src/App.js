import React from 'react'
import Banner from './components/Banner'
import Sidebar from './components/Sidebar'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home'
import List from './components/List'
import Add from './components/Add'
import './App.css'

function App() {
  return (
    <Router>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
      <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet" />
      <Banner />
      <div className='main-content'>
        <Sidebar />
        <div className='content'>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="list/:type" element={<List />} />
            <Route path="add/:type" element={<Add />} />
          </Routes>
        </div>
      </div >
    </Router>
  )
}

export default App