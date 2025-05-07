from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Extract features from form data
        features = []
        for i in range(1, 19):  # Assuming 18 questions
            features.append(int(data.get(f'q{i}', 0)))
        
        # Make prediction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        prob = model.predict_proba(features_array)[0]
        
        # Determine mental health status based on prediction
        if prediction == 0:
            status = "Not Addicted to Social Media"
            advice = "You're maintaining a healthy relationship with social media."
        else:
            status = "Potentially Addicted to Social Media"
            advice = "You may want to consider reducing your social media usage and speaking with a professional."
        
        result = {
            'status': status,
            'advice': advice,
            'confidence': f"{max(prob) * 100:.2f}%"
        }
        
        return render_template('result.html', result=result)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 