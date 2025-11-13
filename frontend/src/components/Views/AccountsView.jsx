/**
 * ACCOUNTS VIEW COMPONENT
 * Vista che mostra tutti i conti bancari con i loro saldi attuali
 */

import React from 'react';
import { calculateAccountBalance } from '../../utils/calculations';
import { accountTypeLabels } from '../../utils/defaultData';

function AccountsView({ accounts, transactions }) {
  return (
    <div className="card">
      <h2>I Tuoi Conti</h2>
      <div className="accounts-grid">
        {accounts.map((acc) => {
          // Calcola il saldo attuale del conto
          const balance = calculateAccountBalance(acc.id, accounts, transactions);

          return (
            <div key={acc.id} className="account-card">
              {/* Tipo di conto */}
              <div className="account-type">
                {accountTypeLabels[acc.type]}
              </div>
              
              {/* Nome del conto */}
              <div className="account-name">{acc.name}</div>
              
              {/* Saldo del conto */}
              <div className="account-balance">€{balance.toFixed(2)}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default AccountsView;
