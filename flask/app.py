from flask import Flask, request, jsonify , send_from_directory
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from flask_cors import CORS

app = Flask(__name__, static_folder='build', static_url_path='')  
CORS(app)

# Load and prepare data
data = pd.read_csv("loan_approval_dataset.csv")
data.columns = data.columns.str.strip()
data = data.drop(columns=['loan_id'])

# Encode fields
encoder = LabelEncoder()
data['education'] = encoder.fit_transform(data['education'].str.strip())
data['self_employed'] = encoder.fit_transform(data['self_employed'].str.strip())
data['loan_status'] = encoder.fit_transform(data['loan_status'].str.strip())

# Maps
education_map = {"Graduate": 0, "Not Graduate": 1}
self_employed_map = {"No": 0, "Yes": 1}

# Train model
X = data.drop('loan_status', axis=1)
y = data['loan_status']
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Feature order for prediction
feature_order = X.columns.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'no_of_dependents': int(request.form['no_of_dependents']),
            'education': education_map[request.form['education']],
            'self_employed': self_employed_map[request.form['self_employed']],
            'income_annum': float(request.form['income_annum']),
            'loan_amount': float(request.form['loan_amount']),
            'loan_term': float(request.form['loan_term']),
            'cibil_score': float(request.form['cibil_score']),
            'residential_assets_value': float(request.form['residential_assets_value']),
            'commercial_assets_value': float(request.form['commercial_assets_value']),
            'luxury_assets_value': float(request.form['luxury_assets_value']),
            'bank_asset_value': float(request.form['bank_asset_value']),
        }

        df = pd.DataFrame([input_data])[feature_order]
        pred = model.predict(df)
        result = encoder.inverse_transform(pred)[0]
        print(result)

        return jsonify({"prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
