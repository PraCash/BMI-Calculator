# Imported the necessary Flask modules.
from flask import Flask, request, render_template

# Defiying the Flask app using 'app = Flask(--name--)'
app = Flask(__name__)


# Creating a route '/' that handles both GET and POST requests.
@app.route("/", methods=["GET", "POST"])
#Adding a 'calculate_bmi' function to calculate BMI.
def calculate_bmi():
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        height_in_meters = height / 100
        bmi = calculate_bmi_value(weight, height_in_meters)
        category = categorize_bmi(bmi)
        return render_template("result.html", bmi=bmi, category=category)
    return render_template("index.html")


def calculate_bmi_value(weight, height):
    return round(weight / (height ** 2), 2)


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    app.run(debug=True)
