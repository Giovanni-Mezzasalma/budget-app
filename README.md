# 💰 Budget App React - Gestione Bilancio Completa

Applicazione React completa per la gestione del bilancio personale con supporto multi-conto, categorie personalizzabili e grafici avanzati.

## 📋 Caratteristiche

- ✅ **Gestione Multi-Conto**: Conti correnti, risparmi, investimenti
- ✅ **Transazioni Complete**: Entrate, spese (necessità/extra), prelievi, trasferimenti
- ✅ **Categorie Personalizzabili**: Crea e modifica le tue categorie
- ✅ **Dashboard con KPI**: Visualizza patrimonio, entrate, uscite e netto
- ✅ **Analisi Avanzata**: Grafici di andamento, distribuzione spese, confronti mensili
- ✅ **Grafici Personalizzati**: Crea grafici custom con periodi e dati personalizzati
- ✅ **Persistenza Dati**: Tutti i dati sono salvati nel browser (localStorage)
- ✅ **Responsive Design**: Ottimizzato per desktop, tablet e mobile

## 🚀 Installazione e Avvio

### Prerequisiti

- Node.js (versione 14 o superiore)
- npm (viene installato con Node.js)

### Passaggi

1. **Installa le dipendenze**:
   ```bash
   npm install
   ```

2. **Avvia l'applicazione in modalità sviluppo**:
   ```bash
   npm start
   ```

3. **Apri il browser**:
   L'applicazione si aprirà automaticamente su [http://localhost:3000](http://localhost:3000)

## 📁 Struttura del Progetto

```
budget-app-react/
├── public/
│   └── index.html              # Template HTML principale
├── src/
│   ├── components/
│   │   ├── Header/             # Componente header con navigazione
│   │   ├── Modals/             # Modali per input dati
│   │   ├── Views/              # Viste principali dell'app
│   │   └── Charts/             # Componenti grafici
│   ├── hooks/
│   │   └── useLocalStorage.js # Hook per persistenza dati
│   ├── utils/
│   │   ├── calculations.js     # Funzioni di calcolo
│   │   ├── chartUtils.js       # Utilità per grafici
│   │   └── defaultData.js      # Dati di default
│   ├── App.jsx                 # Componente principale
│   ├── App.css                 # Stili principali
│   ├── index.js                # Entry point
│   └── index.css               # Stili globali
└── package.json                # Dipendenze del progetto
```

## 🎯 Come Usare l'Applicazione

### 1. Gestione Conti

- Clicca su **"🏦 Gestisci Conti"** per:
  - Visualizzare tutti i tuoi conti con i saldi attuali
  - Aggiungere nuovi conti (corrente, risparmio, investimento)
  - Eliminare conti esistenti

### 2. Aggiungere Transazioni

- **Entrate/Spese**: Clicca su **"💵 Entrata/Spesa"** per registrare:
  - Entrate (stipendio, vendite, ecc.)
  - Spese di necessità (affitto, bollette, spesa)
  - Spese extra (ristoranti, shopping, viaggi)
  - Prelievi

- **Trasferimenti**: Clicca su **"🔄 Trasferimento"** per spostare denaro tra conti

### 3. Personalizzare Categorie

- Clicca su **"📂 Gestisci Categorie"** per:
  - Aggiungere nuove categorie
  - Eliminare categorie esistenti
  - Creare nuovi gruppi di categorie
  - Ripristinare le categorie di default

### 4. Visualizzare i Dati

Usa i **tab di navigazione** per accedere alle diverse viste:

- **📊 Dashboard**: KPI principali (patrimonio, entrate, uscite, netto)
- **🏦 Conti**: Lista di tutti i conti con saldi
- **📝 Transazioni**: Tabella di tutte le transazioni
- **📂 Categorie**: Spese raggruppate per categoria
- **📈 Grafici Personalizzati**: Crea e gestisci grafici custom
- **📊 Analisi**: Statistiche avanzate e confronti

### 5. Creare Grafici Personalizzati

1. Vai al tab **"📈 Grafici Personalizzati"**
2. Clicca su **"+ Nuovo Grafico"**
3. Configura:
   - Titolo del grafico
   - Tipo (linee, barre, torta, ciambella)
   - Periodo (ultimi 3/6/12 mesi, anno corrente, personalizzato)
   - Dati da visualizzare (panoramica, per categoria, per conto)
4. Salva e visualizza il tuo grafico!

## 📊 Selettore Mese/Anno

Usa i **selettori in alto** per filtrare i dati per un mese e anno specifici. Questo influenza:
- Dashboard (KPI mensili)
- Vista Transazioni
- Vista Categorie

## 💾 Persistenza Dati

Tutti i dati sono salvati automaticamente nel **localStorage del browser**:
- ✅ I dati persistono anche dopo la chiusura del browser
- ✅ Nessun server necessario
- ⚠️ I dati sono locali al browser utilizzato
- ⚠️ Cancellare i dati del browser eliminerà i tuoi dati

## 🔧 Build per Produzione

Per creare una versione ottimizzata per il deploy:

```bash
npm run build
```

Questo creerà una cartella `build/` con i file pronti per la pubblicazione.

## 🎨 Personalizzazione

### Modificare i Colori

Puoi personalizzare i colori modificando il file `src/App.css`:
- Gradient principale: `#667eea` → `#764ba2`
- Colore entrate: `#10b981`
- Colore uscite: `#ef4444`
- Colore netto: `#3b82f6`

### Modificare le Categorie di Default

Le categorie predefinite si trovano in `src/utils/defaultData.js`

## 🐛 Troubleshooting

### L'app non si avvia

1. Verifica di aver installato le dipendenze: `npm install`
2. Controlla la versione di Node.js: `node --version` (deve essere >= 14)
3. Prova a cancellare `node_modules` e reinstallare:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

### I dati non vengono salvati

1. Verifica che il localStorage sia abilitato nel browser
2. Controlla la console del browser per eventuali errori (F12)

### Grafici non si visualizzano

1. Verifica che ci siano dati nel periodo selezionato
2. Controlla la console per errori di Chart.js

## 📝 TODO - Prossimi Passi

Come hai menzionato, i prossimi passi per lo sviluppo includono:

- [ ] **Backend Python**: Creare API REST con Flask/Django
- [ ] **Database PostgreSQL**: Migrare da localStorage a PostgreSQL
- [ ] **Sistema di Autenticazione**: Login multi-utente
- [ ] **Deploy**: Hosting su server cloud

## 📄 Licenza

Progetto personale - Tutti i diritti riservati

## 👤 Autore

Giovanni - Chemical Engineer & Developer

---

**Buon bilancio! 💰**
