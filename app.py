from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd # Importa pandas per la generazione del dataset

app = Flask(__name__)

# Carica il modello addestrato
model = joblib.load('linear_regression_model.pkl')

# Genera il dataset simulato (come in km.py)
def generate_dataset():
    np.random.seed(0) # Per riproducibilità
    kilometers = np.random.uniform(0, 200000, 1000)
    # Prezzo base decrescente con i km, più rumore
    prices = 30000 - (kilometers * 0.1) + np.random.normal(0, 5000, 1000)
    # Assicurati che i prezzi non siano negativi
    prices[prices < 0] = 0
    return pd.DataFrame({'Kilometers': kilometers, 'Price': prices})

df = generate_dataset()

@app.route('/')
def index():
    return render_template('predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    kilometers = data['kilometers']

    # Esegui la predizione
    predicted_price = model.predict(np.array([[kilometers]]))[0]

    # Prepara i dati per il grafico scatter
    scatter_data = df[['Kilometers', 'Price']].to_dict(orient='records')
    # Rinomina le chiavi per Chart.js
    scatter_data = [{'x': item['Kilometers'], 'y': item['Price']} for item in scatter_data]

    # Prepara i dati per la retta di regressione
    # Genera punti per la retta su un intervallo di chilometri
    min_km = 0
    max_km = 200000
    line_km = np.array([[i] for i in np.linspace(min_km, max_km, 100)])
    line_prices = model.predict(line_km)
    regression_line_data = [{'x': line_km[i][0], 'y': line_prices[i]} for i in range(len(line_km))]

    # Ottieni coefficiente e intercetta dal modello
    coefficient = model.coef_[0]
    intercept = model.intercept_

    return jsonify({
        'predicted_price': predicted_price,
        'scatter_data': scatter_data,
        'regression_line_data': regression_line_data,
        'coefficient': coefficient,
        'intercept': intercept
    })

if __name__ == '__main__':
    app.run(debug=True)