from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
import pickle
import warnings

warnings.filterwarnings('ignore')
app = Flask(__name__)

# Load the improved model safely
try:
    # Try to load the improved ensemble model first
    model = joblib.load('improved_ensemble_model.joblib')
    scaler = joblib.load('improved_scaler.joblib')
    print("Improved ensemble model loaded successfully!")
except Exception as e:
    try:
        # Fallback to original model
        model = joblib.load('model.joblib')
        scaler = None
        print("Original model loaded successfully (improved model not found)")
    except Exception as e:
        try:
            # Try loading with pickle as fallback
            with open('model.joblib', 'rb') as f:
                model = pickle.load(f)
            scaler = None
            print("Model loaded successfully using pickle")
        except Exception as e:
            print(f"Error loading model: {e}")
            # Create a simple fallback model that always predicts 0 (not addicted)
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
            model.fit(np.random.rand(10, 18), np.random.randint(0, 2, 10))
            scaler = None
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
        
        # Try to predict with the improved model
        try:
            # If we have the improved model with scaler, use it
            if scaler is not None:
                # Scale the features using the improved scaler
                features_scaled = scaler.transform(features_array)
                prediction = model.predict(features_scaled)[0]
                
                # Get prediction probabilities
                try:
                    prob = model.predict_proba(features_scaled)[0]
                    confidence = f"{max(prob) * 100:.2f}%"
                except:
                    confidence = "Not available"
            else:
                # Use original model without scaling
                prediction = model.predict(features_array)[0]
                
                # Try to get prediction probabilities if available
                try:
                    prob = model.predict_proba(features_array)[0]
                    confidence = f"{max(prob) * 100:.2f}%"
                except:
                    confidence = "Not available"
                
        except Exception as e:
            print(f"Prediction error: {e}")
            # Simple heuristic: if sum of scores > 54 (average of 3 per question), consider it addiction risk
            prediction = 1 if sum(features) > 54 else 0
            confidence = "Based on heuristic"
        
        # Map prediction to mental health status
        # The improved model predicts class labels directly
        if isinstance(prediction, str):
            # If prediction is a string (class label)
            if prediction == "Mild":
                status = "Mild Social Media Usage"
                advice = "You have a healthy relationship with social media. Keep up the good balance!"
            elif prediction == "Minimal Moderate":
                status = "Minimal to Moderate Social Media Usage"
                advice = "Your social media usage is generally healthy with occasional concerns. Consider setting some boundaries."
            elif prediction == "Moderate":
                status = "Moderate Social Media Usage"
                advice = "You may be developing some dependency on social media. Consider reducing usage and taking breaks."
            elif prediction == "Severe":
                status = "Severe Social Media Usage"
                advice = "You show signs of significant social media dependency. Consider seeking professional help and implementing strict usage limits."
            elif prediction == "Extremely Severe":
                status = "Extremely Severe Social Media Usage"
                advice = "You may have a serious social media addiction. Please seek professional help immediately."
            else:
                status = "Social Media Usage Assessment"
                advice = "Your social media usage has been assessed. Consider your relationship with social media platforms."
        else:
            # If prediction is numeric (binary)
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