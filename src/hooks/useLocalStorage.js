/**
 * CUSTOM HOOK: useLocalStorage
 * Hook personalizzato per gestire lo stato sincronizzato con localStorage
 * Permette di salvare automaticamente i dati nel browser
 */

import { useState, useEffect } from 'react';

/**
 * Hook per gestire lo stato con persistenza in localStorage
 * @param {string} key - Chiave per il localStorage
 * @param {*} defaultValue - Valore di default se non esiste nel localStorage
 * @returns {Array} - [valore, funzione setter] come useState
 */
function useLocalStorage(key, defaultValue) {
  // Inizializza lo stato leggendo dal localStorage o usando il valore di default
  const [value, setValue] = useState(() => {
    try {
      // Prova a leggere dal localStorage
      const saved = localStorage.getItem(key);
      
      if (saved) {
        // Se esiste, parsifica il JSON
        return JSON.parse(saved);
      }
      
      // Se non esiste, usa il valore di default
      return defaultValue;
    } catch (error) {
      // In caso di errore (es. localStorage non disponibile), usa il default
      console.error(`Error loading ${key} from localStorage:`, error);
      return defaultValue;
    }
  });

  // Effetto che salva nel localStorage ogni volta che il valore cambia
  useEffect(() => {
    try {
      // Salva il valore come JSON nel localStorage
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      // Gestisce eventuali errori (es. quota superata)
      console.error(`Error saving ${key} to localStorage:`, error);
    }
  }, [key, value]); // Esegui quando key o value cambiano

  // Restituisce il valore e la funzione setter (come useState)
  return [value, setValue];
}

export default useLocalStorage;
