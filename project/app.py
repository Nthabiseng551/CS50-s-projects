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

TESTS = []
CONCERNS = []

@app.route("/")
def index():

    return render_template("index.html")

# Define index page for counsellors
@app.route("/counsellor")
def counsellor():

    return render_template("counsellor.html")

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
        counsellor = db.execute("SELECT counsellor FROM users WHERE username=?", request.form.get("username"))[0]["counsellor"]
        if counsellor != 'no':
            return redirect("/")
        else:
            return redirect("/counsellor")# Redirect to counsellors homepage

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

# access to psychological tests
@app.route("/tests")
@login_required
def tests():
    return render_template("tests.html")

# View or post stories about coping and/or surviving psychological disorders
@app.route("/surviving")
@login_required
def surviving():
        return render_template("surviving.html")

# counselling services page
@app.route("/counselling")
@login_required
def counselling():
    return render_template("counselling.html")

#function for users to view their submitted request for counselling
@app.route("/myrequest")
@login_required
def myrequest():
    user_id=session["user_id"]
    users=db.execute("SELECT * FROM users WHERE id=?", user_id)

    # get psychological concerns checked by user on the form(including psychological tests)
    return render_template("myrequest.html", users=users)

# Function for users to cancel their requests for counselling
@app.route("/cancel", methods=["POST"])
@login_required
def cancel():
    id = request.form.get("id")
    username = db.execute("SELECT username FROM users WHERE id=?", id)[0]["username"]
    if id:
        db.execute("UPDATE users SET requests=0 WHERE id=?", id)
        db.execute("DELETE FROM requests WHERE username=?", username)
        flash("Counselling request is cancelled")
    return redirect("/counselling")

# Function and form for users to request for counselling
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
            db.execute("UPDATE requests SET user_email=?, user_number=?, age=?, username=? WHERE username=?", request.form.get("email"), request.form.get("phonenumber"), request.form.get("age"), request.form.get("username"), request.form.get("username"))
            db.execute("UPDATE requests SET counsellor_gender=?, psychological_concerns=?, setting=? WHERE username=?", request.form.get("gender"), request.form.get("concern"), request.form.get("setting"), request.form.get("username"))
            flash("Your request for counselling has been submitted, response time depends on availability of counsellors")
            return render_template("requested.html", users=users)

    else:
        requests = db.execute("SELECT requests FROM users WHERE id=?", user_id)[0]["requests"]
        if requests == 0:
            return render_template("form.html")
        else:
            flash("Each user is allowed one request at a time")
            return render_template("requested.html", users=users)

# Function to desplay counselling requests to "counsellors"
@app.route("/requests")
@login_required
def requests():
    return render_template("requests.html")


# Function for users to volunteer as counsellors
@app.route("/volunteer", methods=["GET", "POST"])
@login_required
def volunteer():
    user_id=session["user_id"]
    users=db.execute("SELECT * FROM users WHERE id=?", user_id)

    if request.method == "POST":

        username = db.execute("SELECT username FROM users WHERE id=?", user_id)[0]["username"]
        #check if username is valid and if user already has request
        if request.form.get("username") != username:
            return apology("please provide your valid username")

        counsellor = db.execute("SELECT counsellor FROM users WHERE username=?", request.form.get("username"))[0]["counsellor"]
        if counsellor != 'no':
            return apology("You have already volunteered!")
        else:
            db.execute("UPDATE users SET counsellor='yes' WHERE username=?", request.form.get("username"))
            flash("Your application for volunteer counsellor has been submitted, thank you for volunteering.")
            return render_template("volunteered.html", users=users)

    else:
        counsellor = db.execute("SELECT counsellor FROM users WHERE id=?", user_id)[0]["counsellor"]
        if counsellor == "no":
            return render_template("volunteer.html")
        else:
            flash("You have already submitted your application to volunteer as a counsellor")
            return render_template("volunteered.html", users=users)


# Function to withdraw volunteering as counsellor application
@app.route("/withdraw", methods=["POST"])
@login_required
def withdraw():
    id = request.form.get("id")
    if id:
        db.execute("UPDATE users SET counsellor='no' WHERE id=?", id)
        flash("Volunteering withdrawn")
    return redirect("/counselling")
