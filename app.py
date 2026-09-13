from flask import Flask, render_template, request
import numpy as np
import joblib

info = joblib.load("california_info.joblib")

model = info["Model"]
columns = info["columns"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", columns=columns)


@app.route("/predict", methods=["POST"])
def predict():

    values = []

    for col in columns:
        value = float(request.form[col])
        values.append(value)

    arr = np.array(values).reshape(1, -1)

    prediction = model.predict(arr)[0]

    return render_template(
        "index.html",
        columns=columns,
        prediction=round(prediction, 3)
    )

if __name__ == "__main__":
    app.run(debug=True)

    