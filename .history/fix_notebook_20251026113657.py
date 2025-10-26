import json
import copy

# Read the notebook
with open('SMMH.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the cell with execution_count 44 (cross-validation cell)
for i, cell in enumerate(nb['cells']):
    if cell.get('execution_count') == 44:
        print(f"Found cross-validation cell at index {i}")
        
        # Get the source lines
        source = cell['source']
        
        # Find the location where we need to add the encoding code
        for j, line in enumerate(source):
            if 'X_data = X_train_aligned' in line:
                # Insert the new code after this line
                new_lines = [
                    '    \n',
                    '    # For XGBoost, transform y_train to start from 0 instead of 1\n',
                    '    y_train_cv = y_train.copy()\n',
                    "    if model_name == 'XGBoost':\n",
                    '        from sklearn.preprocessing import LabelEncoder\n',
                    '        le_cv = LabelEncoder()\n',
                    '        y_train_cv = le_cv.fit_transform(y_train)\n'
                ]
                
                # Insert the new code
                source[j+1:j+1] = new_lines
                
                # Now replace y_train with y_train_cv in cross_val_score
                for k, source_line in enumerate(source):
                    if 'cross_val_score(model, X_data, y_train, cv=cv' in source_line:
                        source[k] = source_line.replace('y_train, cv=cv', 'y_train_cv, cv=cv')
                
        # Update the cell
        nb['cells'][i]['source'] = source
        print("Successfully modified the cross-validation cell")
        break

# Write the notebook back
with open('SMMH.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook has been fixed! XGBoost cross-validation will now work correctly.")

