import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Load the data
home_data = pd.read_csv(iowa_file_path)

# Define target variable
y = home_data.SalePrice

# Define feature columns
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Create feature DataFrame
X = home_data[feature_columns]

# Split data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify and fit the model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)

# Make predictions on validation data
val_predictions = iowa_model.predict(val_X)

# Calculate mean absolute error
val_mae = mean_absolute_error(val_y, val_predictions)
print(f"Validation MAE: {val_mae:,.0f}")

# Print first few predictions and actual values
print("\nFirst few predictions:", iowa_model.predict(val_X.head()))
print("Actual target values:", val_y.head().tolist()) 