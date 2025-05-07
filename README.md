# Social Media Addiction and Mental Health Predictor

## Overview
This project analyzes the relationship between social media usage patterns and mental health indicators. It uses machine learning techniques to identify correlations between social media habits and mental health metrics, and provides a prediction tool to assess potential mental health impacts based on social media usage.

## Features
- Data analysis and visualization of social media usage patterns
- Machine learning models to predict mental health status
- Interactive web application for users to input their social media usage habits and receive mental health assessments
- Comprehensive data visualizations showing correlations between social media usage and mental health indicators
  Follow this link for better demonstration: https://www.linkedin.com/posts/asif2896_social-media-addiction-mental-health-activity-7325887377606914049-UQ8X?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFWZn0wBy8amgZ5P_rDmimf7Ku_0ah84sCg
![Image](https://github.com/user-attachments/assets/e3dcbb7f-19ed-4705-b650-7560ddf8b834)
![Image](https://github.com/user-attachments/assets/c64b984c-f2cd-4ed5-a927-a99abaf67ef6)
![Image](https://github.com/user-attachments/assets/eba453af-2e04-4a46-b110-38aba6c69e91)
![Image](https://github.com/user-attachments/assets/1d33da3d-472a-4646-b5a0-d12dcafcba89)
## Project Structure
- `SMMH.ipynb`: Main Jupyter notebook containing data analysis, preprocessing, and model development
- `diagram.ipynb`: Notebook with visualizations and diagrams showing relationships in the data
- `model.joblib`: Serialized machine learning model for prediction
- `smmh.csv`: Dataset containing survey responses about social media usage and mental health
- `templates/`: HTML templates for the web application
  - `index.html`: Main input form for the web application
  - `result.html`: Results page showing prediction outcomes
- Various PNG files: Visualizations and diagrams generated from the analysis

## Technologies Used
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Jupyter Notebooks for analysis
- Machine Learning (primarily Logistic Regression)
- HTML/CSS/JavaScript for web interface
- Bootstrap for responsive design

## Getting Started

### Prerequisites
- Python 3.7+
- Required Python packages (install via pip):
  ```
  pip install pandas numpy matplotlib seaborn scikit-learn joblib flask
  ```

### Running the Analysis
1. Clone this repository
2. Open and run the `SMMH.ipynb` notebook to see the complete analysis

### Running the Web Application
1. Ensure all dependencies are installed
2. Run the Flask application (the entry point is not visible in the repository but should be created as app.py)
3. Access the application at `http://localhost:5000` in your web browser

## How to Use the Prediction Tool
1. Fill out the form with your information and social media usage habits
2. Submit the form to receive a prediction about your mental health status based on your social media usage patterns
3. Review the recommendations provided based on your results

## Dataset
The project uses a dataset (`smmh.csv`) containing survey responses from individuals about their:
- Demographic information
- Social media usage patterns
- Self-reported mental health indicators

## Model Performance
The machine learning model uses logistic regression to predict mental health status based on social media usage patterns. Performance metrics and visualizations can be viewed in the `SMMH.ipynb` notebook.

## License
This project is licensed under the terms included in the LICENSE file.

## Contributors
- Asif (Project Creator)

## Future Work
- Improve model accuracy with larger and more diverse datasets
- Add more sophisticated prediction models
- Develop personalized recommendations based on prediction results
- Create mobile application version of the prediction tool 
