from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay


app = Flask(__name__)

# Load the model
try:
    model = pickle.load(open('C:\\Users\\HP\\Downloads\\banking_churn\\banking_churn_folder\\customer_churn_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: model.pkl not found. Please run model training script first.")
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize variables
    prediction_class = None
    probability = None
    show_result = False
    error_message = None
    
    if request.method == 'POST':
        try:
            # Get values from the form
            features = {
                'CreditScore': float(request.form['CreditScore']),
                'Age': float(request.form['Age']),
                'Tenure': float(request.form['Tenure']),
                'Balance': float(request.form['Balance']),
                'NumOfProducts': float(request.form['NumOfProducts']),
                'HasCrCard': float(request.form['HasCrCard']),
                'IsActiveMember': float(request.form['IsActiveMember']),
                'EstimatedSalary': float(request.form['EstimatedSalary']),
                'Complain': float(request.form['Complain']),
                'Satisfaction_Score': float(request.form['Satisfaction_Score']),
                'Point_Earned': float(request.form['Point_Earned']),
                'Card_Tier': float(request.form['Card_Tier']),
                'Geography_France': float(request.form['Geography'] == 'France'),
                'Geography_Germany': float(request.form['Geography'] == 'Germany'),
                'Geography_Spain': float(request.form['Geography'] == 'Spain'),
                'Gender_Female': float(request.form['Gender'] == 'Female'),
                'Gender_Male': float(request.form['Gender'] == 'Male')
            }
            
            # Create DataFrame with the features
            final_features = pd.DataFrame([features])
            
            # Get prediction probabilities
            prob = model.predict_proba(final_features)[0]
            churn_probability = prob[1]  # Probability of churning (class 1)
            
            # Format the probability as a percentage
            probability = round(churn_probability * 100)
            
            # Determine if customer will churn (if probability > 0.5)
            prediction_class = "Will Churn" if churn_probability > 0.5 else "Will Not Churn"
            
            show_result = True
            
        except Exception as e:
            error_message = f"Error making prediction: {str(e)}"
            show_result = True
    
    return render_template('index.html', 
                         prediction_class=prediction_class, 
                         probability=probability,
                         show_result=show_result,
                         error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)