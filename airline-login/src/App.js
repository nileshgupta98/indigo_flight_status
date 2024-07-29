// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/login';
import FlightStatus from './components/FlightStatus';
import { AuthProvider } from './components/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route 
            path="/flight-status" 
            element={
              <ProtectedRoute>
                <FlightStatus />
              </ProtectedRoute>
            } 
          />
        </Routes>
      </Router>
    </AuthProvider>
    // <Router>
    //   <Routes>
    //     <Route path="/" element={<Login />} />
    //     <Route path="/flight-status" element={<FlightStatus />} />
    //     {/* Other routes can be added here */}
    //   </Routes>
    // </Router>
  );
};

export default App;