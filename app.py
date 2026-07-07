from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findyourcrop')
def findyourcrop():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        n = float(request.form['N'])
        p = float(request.form['P'])
        k = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        
        input_features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_features)
        
        # BEAUTIFUL RENDER: Pass the crop variable cleanly to result.html
        return render_template('result.html', crop=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
