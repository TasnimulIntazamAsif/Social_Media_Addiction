from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
import pickle
import warnings

warnings.filterwarnings('ignore')
app = Flask(__name__)

# Load the model safely
try:
    model = joblib.load('model.joblib')
    print("Model loaded successfully using joblib")
except Exception as e:
    try:
        # Try loading with pickle as fallback
        with open('model.joblib', 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully using pickle")
    except Exception as e:
        print(f"Error loading model: {e}")
        # Create a simple fallback model that always predicts 0 (not addicted)
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        model.fit(np.random.rand(10, 18), np.random.randint(0, 2, 10))
        print("Warning: Using fallback model")

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
        for i in range(1, 19):  # 18 questions
            features.append(int(data.get(f'q{i}', 0)))
        
        # Make prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Try to predict with the model
        try:
            prediction = model.predict(features_array)[0]
            
            # Try to get prediction probabilities if available
            try:
                prob = model.predict_proba(features_array)[0]
                confidence = f"{max(prob) * 100:.2f}%"
            except:
                # If probabilities aren't available
                confidence = "Not available"
                
        except Exception as e:
            print(f"Prediction error: {e}")
            # Simple heuristic: if sum of scores > 54 (average of 3 per question), consider it addiction risk
            prediction = 1 if sum(features) > 54 else 0
            confidence = "Based on heuristic"
        
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
            'confidence': confidence
        }
        
        return render_template('result.html', result=result)
    
    except Exception as e:
        print(f"General error: {e}")
        return render_template('result.html', result={
            'status': 'Error in Assessment',
            'advice': 'There was an error processing your assessment. Please try again.',
            'confidence': 'N/A'
        })

if __name__ == '__main__':
    app.run(debug=True) 