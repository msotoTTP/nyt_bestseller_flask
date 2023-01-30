from flask import Flask
from flask import render_template
from datetime import date
from main import getBestsellersForDate

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/<year>/<month>/<day>")
def bestsellers(year, month, day):
    try:
        year = int(year)
    except ValueError:
        return "Year must be a number", 400
    try:
        month = int(month)
    except ValueError:
        return "Month must be a number", 400
    try:
        day = int(day)
    except ValueError:
        return "Month must be a number", 400
    try:
        listDate = date(year=year, month=month, day=day)
    except ValueError:
        return "Either year, month, or day out of range", 400
    
    bestsellersList = getBestsellersForDate(listDate)
    return render_template("index.html", bestsellers=bestsellersList, date=listDate.isoformat())