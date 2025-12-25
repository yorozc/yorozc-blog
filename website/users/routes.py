from flask import (Blueprint, request, redirect, url_for, render_template,
                   flash)
from website import bcrypt
from website.database.db import get_users_collection


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
        email = request.form["email"]
        password = request.form["password"]

        #TODO: check if user exists 

        #TODO: validate email and password via regex

        user = {
            "username": username, 
            "email": email, 
            "password": password
        }

        user_coll = get_users_collection()

        user_coll.insert_one(user)
        flash(message="User added", category="success")

        return redirect(url_for("main.index"))

    else:
        return render_template("register.html")