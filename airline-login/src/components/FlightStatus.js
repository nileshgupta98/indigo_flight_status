// src/components/FlightStatus.js
import React, { useState } from 'react';
import axios from 'axios';
import './FlightStatus.css'; // Add your CSS for styling if needed
import logo from '../assets/image002.png';

const FlightStatus = () => {
    const [flightNumber, setFlightNumber] = useState('');
    const [status, setStatus] = useState(null);
    const [error, setError] = useState('');

    const handleCheckStatus = async (e) => {
    e.preventDefault();
    
    try {
        const response = await axios.get(`http://192.168.0.137:5000/flight/status?flight_num=${flightNumber}`);
        console.log(response)
        setStatus(response.data);
        setError('');
    } catch (err) {
        setStatus(null);
        setError('Error fetching flight status');
    }
};

return (
    <>
    <div className="container1">
        <div className="login-container11">
                <img src={logo} alt="Company Logo" className="logo" />
        </div>
        <div className="flight-status-container">
            <h4>Check Flight Status</h4>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleCheckStatus}>
                <div className="form-group">
                    <label htmlFor="flightNumber">Flight Number:</label>
                    <input type="text" id="flightNumber" value={flightNumber} onChange={(e) => setFlightNumber(e.target.value)}required/>
                </div>
                <button type="submit">Check Status</button>
            </form>
            {status && (
                <div className="status-result">
                    <h4>Flight Status:</h4>
                    <table>
                        <thead>
                            <tr>
                                <th>Status</th>
                                <th>Departure Gate</th>
                                <th>Arrival Gate</th>
                                <th>Scheduled Departure</th>
                                <th>Scheduled Arrival</th>
                                <th>Actual Departure</th>
                                <th>Actual Arrival</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{status.data.status}</td>
                                <td>{status.data.departure_gate}</td>
                                <td>{status.data.arrival_gate}</td>
                                <td>{status.data.scheduled_departure}</td>
                                <td>{status.data.scheduled_arrival}</td>
                                <td>{status.data.actual_departure}</td>
                                <td>{status.data.actual_arrival}</td>
                            </tr>
                        </tbody>
                    </table>
                    
                    {/* <p>Status: {status.data.status}</p>
                    <p>Departure Gate: {status.data.departure_gate}</p>
                    <p>Arrival Gate: {status.data.arrival_gate}</p>
                    <p>Scheduled Departure: {status.data.scheduled_departure}</p>
                    <p>Scheduled Arrival: {status.data.scheduled_arrival}</p>
                    <p>Actual Departure: {status.data.actual_departure}</p>
                    <p>Actual Arrival: {status.data.actual_arrival}</p> */}
                </div>)}
        </div>
    </div>
    </>
);
};

export default FlightStatus;
