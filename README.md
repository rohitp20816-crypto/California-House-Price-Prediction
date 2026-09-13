🏠 California House Price Prediction

A machine learning web application that predicts California house prices based on user-provided housing information.

The project uses a trained machine learning model and a Flask web application to provide an easy-to-use interface for making predictions.

🚀 Features
Predict California house prices using a trained ML model.
Simple and user-friendly web interface.
Flask backend for handling predictions.
HTML and CSS frontend.
Pre-trained model/data stored using Joblib.
Easy to run locally.
🛠️ Technologies Used
Python
Flask
Scikit-learn
Pandas
NumPy
Joblib
HTML5
CSS
📁 Project Structure
California-House-Price-Prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── california_info.joblib
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css


If your index.html and style.css are currently in the root folder, move them into the templates and static folders respectively if your Flask application expects the standard Flask project structure.

📄 File Description
File	Description
app.py	Flask application that runs the web server and handles predictions.
train_model.py	Script used to train the machine learning model.
requirements.txt	Contains the Python dependencies required to run the project.
california_info.joblib	Saved machine learning model/data used by the application.
templates/index.html	Frontend HTML page containing the prediction form.
static/style.css	CSS file used to style the web application.
⚙️ Installation
1. Clone the repository
git clone https://github.com/rohitp20816-crypto/California-House-Price-Prediction

2. Navigate to the project directory
cd California-House-Price-Prediction

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate


5. Install dependencies
pip install -r requirements.txt

▶️ Running the Application

Run the Flask application:

python app.py


After starting the application, open the local URL displayed in your terminal, commonly:

http://127.0.0.1:5000/

🧠 Machine Learning Model

The project uses a machine learning model trained using train_model.py.

The trained model/information is saved in:

california_info.joblib


The Flask application loads this file and uses it to generate predictions based on the values entered by the user.

🔄 How It Works
User Input
    ↓
HTML Form
    ↓
Flask Application (app.py)
    ↓
Trained ML Model
    ↓
Price Prediction
    ↓
Result Displayed on Web Page

📊 Model Training

If you need to retrain the model, run:

python train_model.py


This will train the machine learning model and generate/update the required .joblib file.

📦 Dependencies

The required Python packages are listed in:

requirements.txt


Install them using:

pip install -r requirements.txt

📸 Application

🔮 Future Improvements
Improve prediction accuracy through model tuning.
Add data visualization.
Add more input validation.
Deploy the application online.
Add responsive/mobile-friendly design.
Compare multiple machine learning algorithms.
Add interactive charts and statistics.
👨‍💻 Author

Rohit Patil

GitHub: https://github.com/rohitp20816-crypto

⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
