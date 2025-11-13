/**
 * INDEX.JS - Entry point dell'applicazione React
 * Questo file inizializza l'applicazione e la monta nel DOM
 */

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Crea il root e renderizza l'applicazione
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
