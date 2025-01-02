# Customer Churn Prediction Web Application

This project is a **Customer Churn Prediction Web Application** built using Flask for the backend and HTML/CSS (with Bootstrap) for the frontend. The app predicts the likelihood of a customer churning (leaving) based on input features such as their age, credit score, account balance, and more. It provides predictions along with a probability percentage, making it a powerful tool for customer retention strategies.

---

## **Overview**

Customer churn prediction is a critical area in customer relationship management, especially for banking institutions. Retaining customers is often more cost-effective than acquiring new ones. This application leverages a pre-trained machine learning model to predict customer churn based on various demographic, behavioral, and transactional features. 

The application includes:
- A Flask-based backend for handling predictions.
- A user-friendly frontend built with HTML and Bootstrap.
- Dynamic and real-time prediction results with probabilities.

---

## **Features**

1. **Interactive Frontend**:
   - A clean and responsive interface using Bootstrap.
   - Dropdowns, numeric inputs, and radio buttons for easy data entry.
   - Dynamic result display with tailored messages for churn/no-churn predictions.

2. **Flask Backend**:
   - Processes user inputs.
   - Loads the pre-trained machine learning model.
   - Computes churn predictions and probabilities.
   - Handles errors gracefully with user-friendly messages.

3. **Machine Learning Model**:
   - A Random Forest Classifier trained on customer data.
   - Includes hyperparameter tuning using GridSearchCV for optimal performance.
   - Outputs both class predictions and probability scores.

4. **Error Handling**:
   - Checks for missing `model.pkl` and initializes a default model if not found.
   - Catches prediction errors and displays them to the user in a formatted message.

---

## **Project Structure**

The project is organized as follows:

├── templates/ │ └── index.html # HTML template for the web interface  ├── banking_churn.py # Main Flask application ├── customer_churn_model.pkl # Pre-trained machine learning model (to be generated) ├── training.ipynb # For training the model ├── README.md # Project documentation

---

## **Technologies Used**

### **Backend**:
- **Flask**: A lightweight Python web framework for building the backend.
- **pickle**: For loading the pre-trained machine learning model.

### **Frontend**:
- **HTML**: For structuring the user interface.
- **Bootstrap**: For responsive design and styling.

### **Machine Learning**:
- **Random Forest Classifier**: Used for churn prediction.
- **GridSearchCV**: To tune hyperparameters during model training.
- **pandas and numpy**: For data manipulation.

---

## **Installation and Setup**

### Prerequisites
1. Python 3.8 or higher installed.
2. `pip` for installing dependencies.
3. Basic knowledge of running Python scripts.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kudzie99e/customer-churn-prediction.git
   cd banking-churn-app
Install the required libraries:

pip install flask pandas numpy scikit-learn
Ensure the pre-trained model file (customer_churn_model.pkl) is in the project directory. If you don’t have it, train the model using your training script.

Run the Flask application:

python banking_churn.py
Open a web browser and navigate to:
http://127.0.0.1:5000/
Usage Instructions
Input Customer Data:

Fill out the form on the homepage with the customer's details, such as credit score, age, balance, and more.
Select Options:

Choose appropriate values from dropdowns and radio buttons for binary or categorical inputs (e.g., gender, geography, and card tier).
Submit Form:

Click the "Predict Churn" button.
View Results:

The app will display:
Whether the customer will churn or not.
The probability of churn as a percentage.
Results are color-coded for better readability:
Green for "Will Not Churn."
Red for "Will Churn."

Input Features
Feature Name |	Description
CreditScore	Customer's credit score (numeric).
Age	Age of the customer (numeric).
Tenure	Number of years the customer has been with the bank.
Balance	Account balance of the customer (numeric).
NumOfProducts	Number of products the customer uses.
HasCrCard	Whether the customer has a credit card (binary: 0/1).
IsActiveMember	Whether the customer is an active member (binary: 0/1).
EstimatedSalary	Customer's estimated salary (numeric).
Complain	Whether the customer has filed a complaint (binary: 0/1).
Satisfaction_Score	Customer's satisfaction score (numeric).
Point_Earned	Loyalty points earned by the customer (numeric).
Card_Tier	Card type tier: SILVER (1), GOLD (2), DIAMOND (3), PLATINUM (4).
Geography	Customer's location: France, Germany, or Spain.
Gender	Customer's gender: Male or Female.

Future Improvements
Deployment:

Deploy the app to cloud platforms like Heroku, AWS, or Azure for global access.
Database Integration:

Store customer data in a database and allow predictions on existing records.
Model Enhancement:

Train advanced models like Gradient Boosting or Neural Networks.
Implement interpretability tools like SHAP or LIME for better insights.
Enhanced Frontend:

Add charts to visualize feature importance or prediction history.
Improve styling with custom themes and animations.


Prediction Result
Dynamic result display with probabilities and tailored messages.



Acknowledgments
Thanks to open-source libraries like Flask, Bootstrap, and scikit-learn for making this project possible.
Inspired by the need for actionable insights in customer retention for the banking sector.

Contact
For any questions or suggestions, feel free to contact me:

Email: kudzaikaremb@gmail.com
GitHub: kudzie99
