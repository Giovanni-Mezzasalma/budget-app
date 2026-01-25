/**
 * ACCOUNTS VIEW COMPONENT
 * View showing all bank accounts with their current balances
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
          // Calculate the current account balance
          const balance = calculateAccountBalance(acc.id, accounts, transactions);

          return (
            <div key={acc.id} className="account-card">
              {/* Account Type */}
              <div className="account-type">
                {accountTypeLabels[acc.type]}
              </div>
              
              {/* Account Name */}
              <div className="account-name">{acc.name}</div>
              
              {/* Account balance */}
              <div className="account-balance">€{balance.toFixed(2)}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default AccountsView;
