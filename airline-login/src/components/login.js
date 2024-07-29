// src/components/Login.js
import React, { useState, useContext} from 'react';
import axios from 'axios';
import './Login.css'; // You can add CSS to style the form
import logo from '../assets/image001.png';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';

const Login = () => {
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [error, setError] = useState('');
const navigate = useNavigate();
const { login } = useContext(AuthContext);

const handleSubmit = async (e) => {
    e.preventDefault();

    try {
    const response = await axios.post('http://192.168.0.137:5000/users/login', { email, password });
      // Handle success (e.g., save token, redirect)
    console.log('Login successful:', response.data);
    console.log(response.data.status)
    if (response.data.status) {
        // Handle successful login (e.g., save token, redirect)
        login();
        console.log('Login successful!');
        navigate('/flight-status');
    } else {
        setError('Invalid credentials');
    }
    } catch (err) {
    setError('Invalid email or password');
    }
};

return (
    <>
    <div className="container">
        <div className="login-container1">
            <img src={logo} alt="Company Logo" className="logo" />
        </div>
        <div className="login-container">
            <h2>Login</h2>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required/>
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
    
    </>
    
);
};

export default Login;
