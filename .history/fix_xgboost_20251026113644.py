# Fixed cross-validation code for XGBoost
# This is just to show the fix - you'll need to apply it in the notebook

code_to_add = '''
    # For XGBoost, transform y_train to start from 0 instead of 1
    y_train_cv = y_train.copy()
    if model_name == 'XGBoost':
        from sklearn.preprocessing import LabelEncoder
        le_cv = LabelEncoder()
        y_train_cv = le_cv.fit_transform(y_train)
'''

code_to_change = '''
            scores = cross_val_score(model, X_data, y_train_cv, cv=cv, scoring=metric, n_jobs=-1)
'''

print("Add this code after line: 'X_data = X_train_aligned' and before 'model_cv_results = {}'")
print(code_to_add)
print("\n\nChange this line:")
print("from: scores = cross_val_score(model, X_data, y_train, cv=cv, scoring=metric, n_jobs=-1)")
print("to:  " + code_to_change.strip())

