/**
 * INDEX.JS - React Application Entry Point
 * This file initializes the application and mounts it in the DOM.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Root and render the application
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
