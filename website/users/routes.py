from flask import Blueprint, request, redirect, url_for, render_template
from website import bcrypt
from website.database.db import get_db, get_collection


users = Blueprint('users', __name__)

@users.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

    
    else:
        return render_template("login.html")
    
@users.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["username"]
        password = request.form["username"]



    else:
        return render_template("register.html")