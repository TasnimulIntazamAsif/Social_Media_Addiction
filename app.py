from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Convert form data to features array
        features = [
            float(data['age']),
            float(data['gender']),
            float(data['usage_time']),
            float(data['anxiety']),
            float(data['depression']),
            float(data['self_esteem']),
            float(data['sleep_quality'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        
        # Return prediction result
        return jsonify({
            'prediction': int(prediction),
            'message': 'High risk of social media addiction' if prediction == 1 else 'Low risk of social media addiction'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 