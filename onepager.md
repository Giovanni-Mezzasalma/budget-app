# BudgetApp — Documento per potenziale co-founder

Ciao! Questo documento è pensato per spiegarti cos'è BudgetApp, dove siamo arrivati, cosa è previsto nell'MVP e dove voglio portare il progetto nel tempo. È una conversazione onesta, non un pitch.

**Aggiornato:** Marzo 2026

---

## Indice

1. [Da dove viene l'idea](#1-da-dove-viene-lidea)
2. [Cos'è BudgetApp](#2-cosè-budgetapp)
3. [Feature MVP — cosa sarà disponibile al lancio](#3-feature-mvp--cosa-sarà-disponibile-al-lancio)
4. [Sviluppi futuri — la roadmap post-MVP](#4-sviluppi-futuri--la-roadmap-post-mvp)
5. [Stato attuale del progetto](#5-stato-attuale-del-progetto)
6. [Stack tecnologico](#6-stack-tecnologico)
7. [Struttura dei piani (ipotetica)](#7-struttura-dei-piani-ipotetica)
8. [Cosa cerco in un co-founder](#8-cosa-cerco-in-un-co-founder)

---

## 1. Da dove viene l'idea

BudgetApp nasce da un problema personale. Nel tempo avevo costruito tre file Excel separati:

- uno per tracciare entrate e uscite mensili
- uno per monitorare il mio portafoglio investimenti e crypto
- uno per gestire ferie, ROL e permessi in base al mio contratto (CCNL)

Questi tre file non comunicavano tra loro, richiedevano aggiornamento manuale continuo e non erano accessibili ovunque. Ho cominciato a chiedermi: esiste un'app che fa tutto questo, pensata per chi vive e lavora in Italia?

La risposta è no. Le app americane come YNAB ignorano completamente la realtà italiana (CCNL, festività, fatturazione SDI). Le app italiane esistenti coprono un solo pezzo del problema. Da qui è nata l'idea di costruire BudgetApp.

---

## 2. Cos'è BudgetApp

BudgetApp è una piattaforma SaaS di personal finance progettata specificamente per il mercato italiano. L'obiettivo è unire in un'unica app modulare tutto quello che serve per avere una visione finanziaria completa: budget mensile, investimenti, e pianificazione ferie.

Il principio guida è la modularità: ogni utente paga solo per quello che usa, con la possibilità di espandere nel tempo verso funzionalità più avanzate.

La visione a lungo termine prevede due profili utente distinti:

- **Privati (dipendenti):** budget, investimenti, gestione ferie/ROL/permessi secondo CCNL
- **Freelance:** budget, strumenti per lavoro autonomo (fatturazione, clienti, progetti, time tracking)

Per l'MVP ci concentriamo interamente sui privati.

---

## 3. Feature MVP — cosa sarà disponibile al lancio

L'MVP è pensato per il piano Personal, rivolto a dipendenti italiani che vogliono avere controllo sulle proprie finanze.

### 3.1 Gestione conti (Multi-Account)

L'utente può creare e gestire più conti: conto corrente, conto risparmio, carta di credito. Ogni conto ha un saldo aggiornato in tempo reale in base alle transazioni registrate. È supportato anche il trasferimento tra conti.

### 3.2 Transazioni

Registrazione di entrate e uscite con:

- data, importo, descrizione, categoria
- associazione a un conto specifico
- supporto per filtri avanzati (per data, categoria, account, tipo)
- import da file CSV (compatibile con l'export delle principali banche italiane)

### 3.3 Categorie

Categorie predefinite (alimentari, trasporti, salute, ecc.) e categorie personalizzate create dall'utente. Le categorie seguono una struttura gerarchica a due livelli: macro-categoria fissa (Entrate / Spese di Necessità / Spese Extra) e sotto-categorie personalizzabili. Ogni transazione viene associata a una categoria per alimentare analytics e budget.

### 3.4 Budget mensile

L'utente può impostare un budget mensile per ogni categoria di spesa. Le scelte per l'MVP sono deliberatamente semplici:

- solo periodo mensile (no settimanale, no annuale — per ora)
- un budget per categoria (no duplicati)
- solo per le spese (non per le entrate)
- nessun rollover del budget non utilizzato
- nessuna notifica, solo indicatori visivi (🟢 / 🟡 / 🔴) in dashboard

### 3.5 Analytics e report

Dashboard con:

- bilancio mensile (entrate - uscite)
- andamento delle spese per categoria
- confronto tra mesi
### 3.6 Vacation & Leave Planning (killer feature)

Questo è il modulo che differenzia BudgetApp da qualsiasi competitor. Nell'MVP supporta i dipendenti e copre:

**Maturazione automatica:**
- ferie, ROL (Riduzione Orario di Lavoro), permessi extra
- configurabile in base al proprio contratto

**Calcolo festività italiane:**
- festività nazionali fisse
- Pasqua e Pasquetta con calcolo dinamico tramite algoritmo di Butcher
- identificazione automatica dei ponti (es. venerdì tra giovedì festivo e weekend)

**Pianificazione:**
- calendario interattivo per registrare periodi di ferie usufruiti
- visualizzazione del residuo aggiornato
- suggerimento ponti ottimali per massimizzare i giorni di riposo

**Integrazione con il budget (livello leggero):**
- nella dashboard principale compaiono i giorni di ferie disponibili accanto ai dati finanziari
- nessuna automazione avanzata nell'MVP (quella viene dopo)

### 3.7 Autenticazione e sicurezza

- registrazione e login con email e password
- autenticazione JWT
- password hashate con bcrypt
- ogni utente vede solo i propri dati

---

## 4. Sviluppi futuri — la roadmap post-MVP

Queste sono le funzionalità pianificate dopo il lancio dell'MVP. L'ordine riflette la priorità attuale, ma potrebbe cambiare in base al feedback degli utenti.

### 4.1 Personal+ — Investimenti e Crypto

Il secondo piano prevede l'aggiunta di un modulo investimenti:

- tracciamento portafoglio azionario ed ETF
- portafoglio crypto (Bitcoin, Ethereum, ecc.) con prezzi in tempo reale via API (CoinGecko o simili)
- calcolo gain/loss e rendimento percentuale
- asset allocation e grafici di performance
- vista unificata: budget + investimenti + risparmi in una sola dashboard

Questo modulo nasce direttamente dal mio file Excel personale sugli investimenti — già esiste la logica, si tratta di traslarla in un'app.

### 4.2 Ricorrenti e automazioni

- transazioni ricorrenti (stipendio, affitto, abbonamenti)
- notifiche per scadenze e superamento budget
- proiezioni di saldo a fine mese

### 4.3 Integrazione bancaria (Open Banking)

L'MVP usa l'import CSV per recuperare le transazioni dalle banche. Nel medio-lungo termine l'obiettivo è integrare l'import automatico tramite PSD2 (Open Banking europeo), eliminando il data entry manuale.

### 4.4 Mobile App

Dopo la stabilizzazione del frontend web, è prevista un'app mobile in React Native (iOS e Android).

### 4.5 Modulo Freelance

Il piano Freelance è il più ambizioso e viene sviluppato dopo che il prodotto per privati è maturo. Include:

- fatturazione elettronica XML/SDI (regime ordinario e forfettario)
- gestione clienti e progetti
- time tracking
- calendario scadenze fiscali (IVA, IRPEF, contributi INPS)
- per le ferie: logica adattata al lavoro autonomo (giorni non lavorati + impatto su fatturato)

### 4.6 Espansione geografica

La struttura del prodotto è localizzabile. Dopo la validazione sul mercato italiano, l'espansione naturale è Spagna e Francia, adattando i moduli CCNL e fatturazione ai rispettivi sistemi normativi.

### 4.7 Integrazione avanzata ferie ↔ budget

Nell'MVP l'integrazione è "leggera" (solo visibilità condivisa in dashboard). Post-MVP si possono aggiungere:

- creazione automatica di una categoria budget collegata a un periodo di ferie pianificato
- analisi storica: spesa media durante le ferie vs giorni lavorativi
- accantonamento consigliato basato sulle ferie accumulate

### 4.8 AI e automazione

A più lungo termine: categorizzazione automatica delle transazioni, suggerimenti personalizzati, previsioni di spesa basate sullo storico.

---

## 5. Stato attuale del progetto

Il progetto è in sviluppo dal novembre 2025, part-time come unico sviluppatore. Ecco dove siamo:

| Fase | Descrizione | Stato |
|------|-------------|-------|
| 0–3 | Backend core: auth, multi-account, transazioni, categorie, analytics | ✅ Completato |
| 3.8 | Vacation module: ferie/ROL/permessi, festività italiane, ponti | ✅ Completato |
| 3.9 | Budget planning: budget mensili per categoria con tracking real-time | ✅ Completato |
| 3.10 | CSV import | ✅ Completato |
| 4.7–4.8 | Suite Pytest: Budget, CSV (coverage >80%) | ✅ Completato |
| 4.6 | Testing Vacation module | 🔄 In corso |
| 5 | Frontend React — UI completa | ⏳ Pianificato |
| 6 | Deploy produzione (Render + Vercel) | ⏳ Pianificato |

**Beta privata:** Q2 2026 · **Launch pubblico:** Q3 2026

Il backend è completo e testato. La documentazione è mantenuta in `budget-app/docs/` con un file per ogni fase (ARCHITECTURE.md, API_SPEC.md, DEVELOPMENT.md, context.md).

---

## 6. Stack tecnologico

| Layer | Tecnologia |
|-------|-----------|
| Backend | Python 3.12 + FastAPI · SQLAlchemy · PostgreSQL · Alembic |
| Testing | Pytest (coverage >80%) |
| Frontend | React 18 + Vite · TailwindCSS · Axios · Recharts |
| Auth | JWT + bcrypt |
| Infrastructure | Docker Compose · Render (backend) · Vercel (frontend) |
| Database | PostgreSQL con UUID nativi |

---

## 7. Struttura dei piani (ipotetica)

Prezzi indicativi, soggetti a revisione prima del lancio sulla base della validazione con utenti.

| Piano | Prezzo stimato | Cosa include |
|-------|---------------|-------------|
| Personal | ~€2,99/mese | Budget, multi-account, transazioni, ferie/ROL/permessi, CSV import/export, analytics |
| Personal+ | ~€4,99/mese | Tutto di Personal + investment tracking, portafoglio crypto |
| Freelance | ~€9,99/mese | Tutto di Personal+ + fatturazione XML/SDI, clienti, progetti, time tracking |

---

## 8. Cosa cerco in un co-founder

Sono un engineer con background chimico e 7 anni come project engineer, che si è costruito le competenze full-stack da autodidatta. Ho costruito l'intero backend in autonomia. Quello che mi manca — e che cerco in un co-founder — è principalmente:

- **DevOps e scaling:** CI/CD, monitoring, infrastruttura cloud quando il prodotto cresce
- **Esperienza con prodotti SaaS in produzione:** gestione del ciclo di vita oltre lo sviluppo
- **Complementarietà tecnica:** qualcuno che sappia mettere in discussione le scelte architetturali e migliorarle

Non cerco qualcuno che esegua, cerco qualcuno con cui co-costruire. Idealmente con voglia di imparare il business insieme, non solo il codice.

Se vuoi vedere il codice, posso mostrarti il repository. Se hai domande, sono disponibile per una call.

---

*Documento riservato — uso interno — Giovanni Mezzasalma · Marzo 2026*
