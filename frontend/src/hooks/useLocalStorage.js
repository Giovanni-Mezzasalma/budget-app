/**
 * CUSTOM HOOK: useLocalStorage
 * Custom hook to manage the state synchronized with localStorage
 * Allows data to be automatically saved in the browser
 */

import { useState, useEffect } from 'react';

/**
 * Hook to manage state with persistence in localStorage
 * @param {string} key - Key for localStorage
 * @param {*} defaultValue - Default value if it does not exist in localStorage
 * @returns {Array} - [value, setter function] as useState
 */
function useLocalStorage(key, defaultValue) {
  // Initialize the state by reading from localStorage or using the default value
  const [value, setValue] = useState(() => {
    try {
      // Try reading from localStorage
      const saved = localStorage.getItem(key);
      
      if (saved) {
        // If it exists, parse the JSON
        return JSON.parse(saved);
      }
      
      // If it doesn't exist, use the default value
      return defaultValue;
    } catch (error) {
      // In case of error (e.g. localStorage not available), use the default
      console.error(`Error loading ${key} from localStorage:`, error);
      return defaultValue;
    }
  });

  // Effect that saves to localStorage every time the value changes
  useEffect(() => {
    try {
      // Save the value as JSON in localStorage
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      // Handles any errors (e.g. quota exceeded)
      console.error(`Error saving ${key} to localStorage:`, error);
    }
  }, [key, value]); // Esegui quando key o value cambiano

  // Returns the value and the setter function (like useState)
  return [value, setValue];
}

export default useLocalStorage;
