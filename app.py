from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Initialize the Flask application
app = Flask(__name__)

# PERMANENT FIX: Dynamically find the absolute path of the directory containing app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

# Load the trained machine learning model using the absolute path
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

# Route for the Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for rendering the prediction form (FindYourCrop)
@app.route('/findyourcrop')
def findyourcrop():
    return render_template('predict.html')

# Route for processing the form submission and generating crop recommendations
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve agricultural parameters entered by the user
        n = float(request.form['N'])
        p = float(request.form['P'])
        k = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        
        # Format the parameters as an array for the model
        input_features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        
        # Pass values to the trained machine learning model using the predict() function
        prediction = model.predict(input_features)
        
        # Display the result to the user
        return f"<h2>The recommended crop for the given climatic conditions is: <span style='color: green;'>{prediction[0]}</span></h2><br><a href='/findyourcrop'>Go Back</a>"

# Main function to run the application on the local development server
if __name__ == '__main__':
    app.run(debug=True)
