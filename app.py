import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///yalies.db")

@app.route("/")
def home():
    if request.method == "GET":
        # Change feat to id of whatever restaurant will be featured
        feat = 3
        featdb = db.execute("SELECT * FROM restaurants WHERE id=?", feat)
        featid = db.execute("SELECT id FROM restaurants WHERE id=?", feat)
        featid = featid[0]["id"]
        # Change id inputs to id of whatever other restaurants will be featured
        restdb = db.execute("SELECT * FROM restaurants WHERE id=? OR id=? OR id=? OR id=? OR id=?", 1, 7, 8, 12, 9)
        restid = db.execute("SELECT id FROM restaurants WHERE id=? OR id=? OR id=? OR id=? OR id=?", 1, 7, 8, 12, 9 )
        restid = restid[0]["id"]
        return render_template("home.html", restdb=restdb, restid=restid, featdb=featdb, featid=featid)
    else:
        return render_template("home.html")

@app.route("/explore", methods=["GET", "POST"])
def explore():
    if request.method == "GET":
        restdb = db.execute("SELECT * FROM restaurants")
        restid = db.execute("SELECT id FROM restaurants")
        restid = restid[0]["id"]
        return render_template("explore.html", restdb=restdb, restid=restid)
    else:
        restdb = db.execute("SELECT * FROM restaurants")
        restid = db.execute("SELECT id FROM restaurants")
        restid = restid[0]["id"]
        if not request.form.get("restaurant"):
            return render_template("explore.html", restdb=restdb, restid=restid)
        else:
            restaurant = request.form.get("restaurant")
            restdb = db.execute("SELECT * FROM restaurants WHERE restaurant LIKE ?", "%" + restaurant + "%")
            restid = db.execute("SELECT id FROM restaurants WHERE restaurant LIKE ?", "%" + restaurant + "%")
            try:
                restid = restid[0]["id"]
                return render_template("explore.html", restdb=restdb, restid=restid)
            except IndexError: 
                return render_template("searchapology.html")
        

@app.route("/randomize", methods=["GET", "POST"])
def randomize():
    if request.method == "GET":
        randomid = random.randint(1, 12)
        print(randomid)
        restdb = db.execute("SELECT * FROM restaurants WHERE id = ?", randomid)
        restid = db.execute("SELECT id FROM restaurants WHERE id = ?", randomid)
        restid = restid[0]["id"]
        return render_template("randomize.html", restdb=restdb, restid=restid)
    else:
        return render_template("randomize.html")

@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    if request.method == "GET":
        return render_template("suggest.html")
    else:
        return render_template("suggest.html")