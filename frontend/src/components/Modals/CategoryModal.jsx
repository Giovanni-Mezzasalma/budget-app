/**
 * CATEGORY MODAL COMPONENT
 * Modal for managing categories and subcategories:
 * - View categories by type
 * - Add new categories
 * - Delete categories
 * - Add/delete groups
 * - Restore default categories
 */

import React, { useState } from 'react';
import { categoryTypeLabels } from '../../utils/defaultData';

function CategoryModal({ isOpen, onClose, categories, onUpdateCategories, onResetCategories }) {
  // State to keep track of input values
  const [inputValues, setInputValues] = useState({});

  /**
   * Adds a simple category (array)
   */
  const addSimpleCategory = (type) => {
    const value = inputValues[`new-${type}`]?.trim();
    
    if (value) {
      const newCategories = { ...categories };
      newCategories[type].push(value);
      onUpdateCategories(newCategories);
      
      // Reset input
      setInputValues(prev => ({ ...prev, [`new-${type}`]: '' }));
    }
  };

  /**
   * Removes a simple category (array)
   */
  const removeSimpleCategory = (type, index) => {
    if (window.confirm('Sei sicuro di voler eliminare questa categoria?')) {
      const newCategories = { ...categories };
      newCategories[type].splice(index, 1);
      onUpdateCategories(newCategories);
    }
  };

  /**
   * Add a subcategory to a group
   */
  const addGroupCategory = (type, group) => {
    const value = inputValues[`new-${type}-${group}`]?.trim();
    
    if (value) {
      const newCategories = { ...categories };
      newCategories[type][group].push(value);
      onUpdateCategories(newCategories);
      
      // Reset input
      setInputValues(prev => ({ ...prev, [`new-${type}-${group}`]: '' }));
    }
  };

  /**
   * Removes a subcategory from a group
   */
  const removeGroupCategory = (type, group, index) => {
    if (window.confirm('Sei sicuro di voler eliminare questa sottocategoria?')) {
      const newCategories = { ...categories };
      newCategories[type][group].splice(index, 1);
      onUpdateCategories(newCategories);
    }
  };

  /**
   * Add a new group
   */
  const addNewGroup = (type) => {
    const value = inputValues[`new-group-${type}`]?.trim();
    
    if (value) {
      const newCategories = { ...categories };
      newCategories[type][value] = [];
      onUpdateCategories(newCategories);
      
      // Reset input
      setInputValues(prev => ({ ...prev, [`new-group-${type}`]: '' }));
    }
  };

  /**
   * Removes an entire group
   */
  const removeGroup = (type, group) => {
    if (window.confirm(`Sei sicuro di voler eliminare il gruppo "${group}" e tutte le sue sottocategorie?`)) {
      const newCategories = { ...categories };
      delete newCategories[type][group];
      onUpdateCategories(newCategories);
    }
  };

  /**
   * Handles changes in inputs
   */
  const handleInputChange = (key, value) => {
    setInputValues(prev => ({ ...prev, [key]: value }));
  };

  // If the modal is not open, it does not render anything
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Gestisci Categorie e Sottocategorie</h2>
          <button className="close-btn" onClick={onClose}>&times;</button>
        </div>

        {/* Button to restore default categories */}
        <div style={{ marginBottom: '20px' }}>
          <button className="btn btn-secondary btn-small" onClick={onResetCategories}>
            🔄 Ripristina Categorie di Default
          </button>
        </div>

        {/* Category Manager */}
        <div className="category-manager">
          {Object.keys(categories).map((type) => {
            const cats = categories[type];
            const isArray = Array.isArray(cats);

            return (
              <div key={type} className="category-section">
                <h4>{categoryTypeLabels[type]}</h4>

                {isArray ? (
                  // Simple categories (array)
                  <>
                    <div className="subcategory-list">
                      {cats.map((cat, index) => (
                        <div key={index} className="subcategory-item">
                          <span>{cat}</span>
                          <button
                            type="button"
                            onClick={() => removeSimpleCategory(type, index)}
                          >
                            ×
                          </button>
                        </div>
                      ))}
                    </div>
                    <div className="add-subcategory">
                      <input
                        type="text"
                        value={inputValues[`new-${type}`] || ''}
                        onChange={(e) => handleInputChange(`new-${type}`, e.target.value)}
                        placeholder="Nuova categoria"
                      />
                      <button
                        type="button"
                        className="btn btn-primary btn-small"
                        onClick={() => addSimpleCategory(type)}
                      >
                        Aggiungi
                      </button>
                    </div>
                  </>
                ) : (
                  // Categories with groups (object)
                  <>
                    {Object.keys(cats).map((group) => (
                      <div
                        key={group}
                        style={{
                          margin: '15px 0',
                          padding: '15px',
                          background: 'white',
                          borderRadius: '10px'
                        }}
                      >
                        <div
                          style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            marginBottom: '10px'
                          }}
                        >
                          <strong>{group}</strong>
                          <button
                            type="button"
                            className="btn-danger btn-small"
                            onClick={() => removeGroup(type, group)}
                          >
                            Elimina Gruppo
                          </button>
                        </div>

                        <div className="subcategory-list">
                          {cats[group].map((subcat, index) => (
                            <div key={index} className="subcategory-item">
                              <span>{subcat}</span>
                              <button
                                type="button"
                                onClick={() => removeGroupCategory(type, group, index)}
                              >
                                ×
                              </button>
                            </div>
                          ))}
                        </div>

                        <div className="add-subcategory">
                          <input
                            type="text"
                            value={inputValues[`new-${type}-${group}`] || ''}
                            onChange={(e) =>
                              handleInputChange(`new-${type}-${group}`, e.target.value)
                            }
                            placeholder="Nuova sottocategoria"
                          />
                          <button
                            type="button"
                            className="btn btn-primary btn-small"
                            onClick={() => addGroupCategory(type, group)}
                          >
                            Aggiungi
                          </button>
                        </div>
                      </div>
                    ))}

                    {/* Form to add a new group */}
                    <div style={{ marginTop: '15px' }}>
                      <div className="add-subcategory">
                        <input
                          type="text"
                          value={inputValues[`new-group-${type}`] || ''}
                          onChange={(e) =>
                            handleInputChange(`new-group-${type}`, e.target.value)
                          }
                          placeholder="Nome nuovo gruppo"
                        />
                        <button
                          type="button"
                          className="btn btn-success btn-small"
                          onClick={() => addNewGroup(type)}
                        >
                          Aggiungi Gruppo
                        </button>
                      </div>
                    </div>
                  </>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default CategoryModal;
