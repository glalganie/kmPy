import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from flask import Flask, request, jsonify, render_template
# Creazione del dataset
np.random.seed(42)
n = 1000  # Numero di auto
km = np.random.randint(0, 200001, size=n)  # Chilometraggio da 0 a 200.000 km
noise = np.random.randn(n) * 2000  # Rumore random per rendere il modello più realistico
price = 30000 - km * 0.05 + noise  # Relazione tra chilometri e prezzo, con rumore

# Creazione del DataFrame
data = pd.DataFrame({'km': km, 'price': price})

# Visualizzazione iniziale dei dati
plt.figure(figsize=(8, 6))
plt.scatter(data['km'], data['price'], color='blue', alpha=0.5, label='Dati di auto')
plt.title("Chilometraggio vs Prezzo dell'auto")
plt.xlabel("Chilometraggio (km)")
plt.ylabel("Prezzo (€)")
plt.show()

# Divisione dei dati in training e test set
X = data[['km']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Predizione dei prezzi
y_pred = model.predict(X_test)

# Visualizzazione della retta di regressione
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Dati di test')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Retta di regressione')
#plt.plot(X_test, y_pred, color='red', linewidth=2, label='Retta di regressione')
plt.title("Chilometraggio vs Prezzo dell'auto con Regressione Lineare")
plt.xlabel("Chilometraggio (km)")
plt.ylabel("Prezzo (€)")
plt.legend()
plt.show()

# Coefficiente della retta
print(f"Coefficiente angolare (m): {model.coef_[0]}")
print(f"Intercetta (b): {model.intercept_}")


joblib.dump(model, 'linear_regression_model.pkl') 

app = Flask(__name__)

# Carica il modello addestrato
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def index():
    return render_template('predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    kilometers = data['kilometers']

    # Esegui la predizione
    predicted_price = model.predict(np.array([[kilometers]]))[0]

    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)