from flask import Blueprint, request, redirect, url_for, render_template
from website import bcrypt


users = Blueprint('users', __name__)

@users.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

    
    else:
        return render_template("login.html")