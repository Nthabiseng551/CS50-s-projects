import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user id
    session.clear()

    # User reached route via POST by submitting form

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Username required")

        elif not request.form.get("password"):
            return apology("Password required")

        elif not request.form.get("confirmation"):
            return apology("Re-enter password to confirm")

        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("Passwords do not match")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 0:
            return apology("Username already exist, try another one")

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )

        # recently inserted user
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]

        # Redirect to homepage
        return redirect("/")

    # User reached route via GET through URL or redirect
    else:
        return render_template("register.html")

@app.route("/tests")
@login_required
def tests():
    return render_template("tests.html")


@app.route("/surviving")
@login_required
def surviving():
        return render_template("surviving.html")

@app.route("/counselling")
@login_required
def counselling():
    return render_template("counselling.html")


@app.route("/cancel", methods=["POST"])
@login_required
def cancel():
    id = request.form.get("id")
    if id:
        db.execute("UPDATE users SET requests=0 WHERE id=?", id)
        flash("Counselling request is cancelled")
    return redirect("/counselling")

@app.route("/form", methods=["GET", "POST"])
@login_required
def form():
    user_id=session["user_id"]
    users=db.execute("SELECT * FROM users WHERE id=?", user_id)

    if request.method == "POST":

        username = db.execute("SELECT username FROM users WHERE id=?", user_id)[0]["username"]
        #check if username is valid and if user already has request
        if request.form.get("username") != username:
            return apology("please provide your valid username")

        # query database for request status of user and usernames
        requests = db.execute("SELECT requests FROM users WHERE username=?", request.form.get("username"))[0]["requests"]

        if requests != 0:
            return apology("Each user is allowed one request at a time")

        else:
            db.execute("UPDATE users SET requests=1 WHERE username=?", request.form.get("username"))
            flash("Your request for counselling has been submitted, response time depends on availability of counsellors")
            return render_template("requested.html", users=users)

    else:
        requests = db.execute("SELECT requests FROM users WHERE id=?", user_id)[0]["requests"]
        if requests == 0:
            return render_template("form.html")
        else:
            flash("Each user is allowed one request at a time")
            return render_template("requested.html", users=users)


@app.route("/requests", methods=["GET", "POST"])
@login_required
def requests():
    

