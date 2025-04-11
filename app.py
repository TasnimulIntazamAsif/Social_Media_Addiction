from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data from the request
        data = request.form.to_dict()
        
        # Create a dictionary with all features initialized to 0 or appropriate defaults
        features = {}
        
        # Initialize all features from the model with zeros
        for feature_name in model.feature_names_in_:
            features[feature_name] = 0
        
        # Now set the values for the features we have from the form
        features['Age'] = float(data.get('age', 0))
        features['SM_Usage_Without_Purpose'] = int(data.get('sm_usage_without_purpose', 0))
        features['SM_Distraction'] = int(data.get('sm_distraction', 0))
        features['Restless_Without_SM'] = int(data.get('restless_without_sm', 0))
        features['Easily_Distracted'] = int(data.get('easily_distracted', 0))
        features['Bothered_By_Worries'] = int(data.get('bothered_by_worries', 0))
        features['Difficulty_Concentrating'] = int(data.get('difficult_to_concentrate', 0))
        features['Comparison_On_SM'] = int(data.get('compare_to_others', 0))
        features['Feelings_About_Comparison'] = 3  # Default value
        features['Seeking_Validation_SM'] = int(data.get('seek_validation', 0))
        features['Depression_Frequency'] = int(data.get('feel_depressed', 0))
        features['Interest_Fluctuation'] = int(data.get('interest_fluctuation', 0))
        features['Sleep_Issues'] = int(data.get('sleep_issues', 0))
        
        # Set default values for categorical variables
        features['Gender_Female'] = 1  # Assuming female as default
        features['Relationship_Status_Single'] = 1  # Assuming single as default
        features['Occupation_Status_University Student'] = 1  # Assuming university student
        features['Affiliation_Type_University'] = 1  # Assuming university
        features['Uses_Social_Media_Yes'] = 1  # Assuming uses social media
        features['Common_Platforms_Facebook, Instagram, YouTube'] = 1  # Common platforms
        features['Daily_SM_Usage_Between 2 and 3 hours'] = 1  # Daily usage
        
        # Create DataFrame with features in the exact order expected by the model
        input_df = pd.DataFrame([features])[model.feature_names_in_]
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        print(f"Prediction value: {prediction}")
        
        # Map prediction to mental status - handle any possible prediction value
        if prediction == 0:
            mental_status = 'Good'
        elif prediction == 1:
            mental_status = 'Moderate'
        else:
            mental_status = 'Poor'
        
        return render_template('result.html', prediction=mental_status)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
