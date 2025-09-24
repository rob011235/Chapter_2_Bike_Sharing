from flask import Flask, render_template, request
from webapp.bike_calc import calc_bike_rentals

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    holiday = request.form.get("isHoliday") == "on"
    season = int(request.form.get("season"))
    temp = float(request.form.get("temp"))
    bike_rentals = calc_bike_rentals(holiday, season, temp)
    return render_template("results.html", rentals=bike_rentals)
