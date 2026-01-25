/**
 * DEFAULT DATA
 * Contains all the default data for the application:
 * - Default categories (income, essential expenses, extra expenses, withdrawals)
 * - Default bank accounts
 */

// Default categories organized by transaction type
export const defaultCategories = {
  // Categories for income (simple array)
  income: [
    'Reddito Principale',
    'Reddito Secondario',
    'Affitto',
    'Vendita',
    'Altro'
  ],
  
  // Categories for essential expenses (organized into groups)
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
  
  // Categories for extra expenses (organized into groups)
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
  
  // Category for withdrawals
  'withdrawal': ['Prelievo']
};

// Default bank accounts
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

// Account Type Labels (for display)
export const accountTypeLabels = {
  'current': 'Corrente',
  'savings': 'Risparmio',
  'investment': 'Investimento'
};

// Transaction type labels (for display)
export const transactionTypeLabels = {
  'income': 'Entrata',
  'expense-necessity': 'Necessità',
  'expense-extra': 'Extra',
  'withdrawal': 'Prelievo'
};

// Labels for category types (used in the category modal)
export const categoryTypeLabels = {
  'income': 'Entrate',
  'expense-necessity': 'Spese di Necessità',
  'expense-extra': 'Spese Extra',
  'withdrawal': 'Prelievi'
};
