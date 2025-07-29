# Predittore Prezzo Auto - Realizzato con Trae

Questo progetto implementa un predittore del prezzo delle auto basato sui chilometri percorsi, utilizzando un modello di regressione lineare. L'applicazione è composta da un backend Flask che serve un'interfaccia web e gestisce le previsioni, e un frontend HTML/CSS/JavaScript che visualizza i risultati e un grafico interattivo.


![KM](https://github.com/user-attachments/assets/f43aaf22-54b2-4cbe-9fe5-2655d40f5d3f)

## Caratteristiche

- **Generazione Dataset**: Il file `km.py` genera un dataset simulato di 1000 auto con chilometraggio variabile e prezzi correlati.
- **Regressione Lineare**: Un modello di regressione lineare viene addestrato sul dataset per prevedere il prezzo dell'auto in base ai chilometri.
- **Backend Flask**: Un server web leggero (`app.py`) che carica il modello addestrato, serve l'interfaccia utente e fornisce un'API per le previsioni.
- **Interfaccia Web Interattiva**: `predictor.html` offre un'interfaccia utente per inserire i chilometri, ottenere una previsione del prezzo e visualizzare un grafico che mostra i dati simulati e la retta di regressione.
- **Visualizzazione Grafica**: Utilizza Chart.js per visualizzare la relazione tra chilometri e prezzo, inclusa la retta di regressione.

## Struttura del Progetto
kmPy/
├── .venv/                  # Ambiente virtuale Python
├── app.py                  # Backend Flask per il predittore
├── km.py                   # Script per la generazione del dataset e l'addestramento del modello
├── linear_regression_model.pkl # Modello di regressione lineare salvato
└── templates/
└── predictor.html      # Interfaccia utente web


## Configurazione e Avvio

Segui questi passaggi per configurare ed eseguire il progetto.

### 1. Clona il Repository (o assicurati di avere i file)

Assicurati di avere tutti i file del progetto nella directory `c:\Users\PercorsoUtente\Desktop\kmPy\`.

### 2. Configura l'Ambiente Virtuale

È consigliabile utilizzare un ambiente virtuale per gestire le dipendenze del progetto.

Apri il terminale nella directory `c:\Users\PercorsoUtente\Desktop\kmPy\` ed esegui:

```bash
python -m venv .venv
```

### 3. Attiva l'Ambiente Virtuale

**Su Windows:**

```bash
.venv\Scripts\activate
```

### 4. Installa le Dipendenze

Con l'ambiente virtuale attivo, installa le librerie necessarie:

```bash
pip install numpy pandas matplotlib scikit-learn Flask joblib
```

### 5. Genera il Modello di Regressione

Esegui lo script `km.py` una volta per generare il dataset e salvare il modello addestrato come `linear_regression_model.pkl`.

```bash
python km.py
```

### 6. Avvia il Server Flask

Avvia l'applicazione web Flask. Assicurati che il file `predictor.html` si trovi nella sottocartella `templates`.

```bash
python app.py
```

### 7. Accedi all'Applicazione

Una volta che il server Flask è in esecuzione, apri il tuo browser web e vai a:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Qui potrai inserire i chilometri e ottenere una previsione del prezzo dell'auto, visualizzando anche il grafico della regressione.

## Utilizzo

1. Apri l'applicazione nel tuo browser.
2. Inserisci il numero di chilometri nel campo "Chilometri percorsi:".
3. Clicca su "Calcola Prezzo" per ottenere la previsione.
4. Il prezzo stimato, il coefficiente e l'intercetta del modello verranno visualizzati, insieme a un grafico che mostra i dati simulati e la retta di regressione.

## Risoluzione Problemi Comuni

- **`ModuleNotFoundError`**: Assicurati di aver attivato l'ambiente virtuale e installato tutte le dipendenze (`pip install ...`).
- **`TemplateNotFound: predictor.html`**: Assicurati che `predictor.html` si trovi nella cartella `templates` all'interno della directory del progetto.
- **Previsione non risponde / Grafico non appare**: Verifica la console del browser per errori JavaScript e la console del server Flask per errori Python. Assicurati che il file `predictor.html` sia stato aggiornato con il codice più recente fornito.






