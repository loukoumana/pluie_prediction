from flask import Flask, render_template, request, jsonify
from joblib import load

app = Flask(__name__)

# Charger le modèle préalablement enregistré
model = load('modele_prediction_pluie.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtenir les données d'entrée depuis la requête POST
        data = request.form.to_dict()

        # Effectuer la prédiction avec le modèle
        prediction = model.predict([[float(data['Temperature']), float(data['Humidity']), float(data['Wind_Speed']), float(data['Wind_Bearing']), float(data['Visibility']), float(data['Pressure'])]])

        # Retourner la prédiction à la page HTML
        return render_template('index.html', prediction=int(prediction[0]))

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
