/**
 * DEFAULT DATA
 * Contiene tutti i dati di default per l'applicazione:
 * - Categorie predefinite (entrate, spese necessità, spese extra, prelievi)
 * - Conti bancari di default
 */

// Categorie di default organizzate per tipo di transazione
export const defaultCategories = {
  // Categorie per le entrate (array semplice)
  income: [
    'Reddito Principale',
    'Reddito Secondario',
    'Affitto',
    'Vendita',
    'Altro'
  ],
  
  // Categorie per le spese di necessità (organizzate in gruppi)
  'expense-necessity': {
    'Casa': [
      'Mutuo/Affitto',
      'Elettricità',
      'Gas',
      'Acqua',
      'Manutenzione Casa',
      'Tasse',
      'Telefono/Internet',
      'Assicurazione Casa',
      'Spesa/Cibo'
    ],
    'Trasporti': [
      'Rate auto',
      'Assicurazione Auto',
      'Benzina',
      'Manutenzione',
      'Bollo',
      'Pedaggi',
      'Parcheggi',
      'Mezzi pubblici',
      'Multa'
    ],
    'Salute': [
      'Medicinali',
      'Polizze',
      'Visite mediche/esami',
      'Sport',
      'Occhiali/Lenti'
    ],
    'Figli': [
      'Scuola',
      'Abbigliamento',
      'Attività extra',
      'Babysitting'
    ],
    'Istruzione': [
      'Retta scolastica',
      'Libri scolastici',
      'Formazione'
    ],
    'Altro': [
      'Abbigliamento/Calzature',
      'Rate prestito',
      'Rate carta di credito',
      'Una tantum'
    ]
  },
  
  // Categorie per le spese extra (organizzate in gruppi)
  'expense-extra': {
    'Svago': [
      'Ristorazione',
      'Bar',
      'Cinema/Uscite/Eventi',
      'Abbonamenti digitali',
      'Cura personale',
      'Donazioni e Regali',
      'Divertimento',
      'Fumo',
      'Arredamento',
      'Cultura',
      'Viaggi',
      'Shopping'
    ],
    'Animali': [
      'Cibo',
      'Veterinario'
    ]
  },
  
  // Categoria per i prelievi
  'withdrawal': ['Prelievo']
};

// Conti bancari predefiniti
export const defaultAccounts = [
  {
    id: 1,
    name: 'N26',
    type: 'current',
    initialBalance: 0
  },
  {
    id: 2,
    name: 'Intesa SanPaolo',
    type: 'current',
    initialBalance: 0
  },
  {
    id: 3,
    name: 'Revolut',
    type: 'current',
    initialBalance: 0
  },
  {
    id: 4,
    name: 'PayPal',
    type: 'current',
    initialBalance: 0
  }
];

// Etichette per i tipi di conto (per la visualizzazione)
export const accountTypeLabels = {
  'current': 'Corrente',
  'savings': 'Risparmio',
  'investment': 'Investimento'
};

// Etichette per i tipi di transazione (per la visualizzazione)
export const transactionTypeLabels = {
  'income': 'Entrata',
  'expense-necessity': 'Necessità',
  'expense-extra': 'Extra',
  'withdrawal': 'Prelievo'
};

// Etichette per i tipi di categoria (usate nel modal categorie)
export const categoryTypeLabels = {
  'income': 'Entrate',
  'expense-necessity': 'Spese di Necessità',
  'expense-extra': 'Spese Extra',
  'withdrawal': 'Prelievi'
};
