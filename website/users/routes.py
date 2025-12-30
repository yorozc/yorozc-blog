from flask import (Blueprint, request, redirect, url_for, render_template,
                   flash)
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from website.database.db import get_users_collection
from website.models.user import User

users = Blueprint('users', __name__)

# TODO: Add better error handling

@users.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]
            remember = False # used for "remember me" chckbox
            if request.form["password"]:
                remember = True

        except Exception as e:
            print(f"Error: {e}")

        users = get_users_collection()

        doc = users.find_one({"email": email})

        if doc and check_password_hash(doc["password"], password): # user found

            if check_password_hash(doc["password"], password):
                user = User(doc)
                login_user(user, remember=remember) # true or false
                flash(f"User {user.username} Found. Logging in now!", category="success")
                return redirect(url_for("main.index"))
            
            else: #wrong password
                flash("Wrong password!", category="error")
                return redirect(url_for("users.login"))

        else:
            flash("User not found!", category="error")
            return redirect(url_for("users.login"))
        
    else:
        return render_template("login.html")

@login_required
@users.route("/logout")
def logout():
    logout_user()
    flash("Successfully logged out!", category="success")
    return redirect(url_for("main.index"))
    
@users.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        hashed_password = generate_password_hash(request.form["password"], method="scrypt", salt_length=16)
        user_coll = get_users_collection() 

        #TODO: validate email and password via regex

        user = {
            "username": username, 
            "email": email, 
            "password": hashed_password,
            "role": "user"
        }

        # check if user exists and stop duplicates
        doc = user_coll.find_one({
            "$or": [
                {"email": email}, 
                {"username": username}
                ]
            })

        if doc:
            if doc["username"] == username:
                flash("Username already taken!", category="error")
        
            else:
                flash("Email already exists, login instead", category="error")
                
            return redirect(url_for("users.login"))
        
        else:
        # success case 
            try:
                user_coll.insert_one(user) # adds user to db
                doc = user_coll.find_one({"email": email}) # finds recently made user to make into User obj
                flash(message=f"User {username} created!", category="success")
                user = User(doc) 
                login_user(user, remember=True)
                return redirect(url_for("main.index"))
            
            except Exception as e:
                return f"ERROR:{e}"
        
    else:
        return render_template("register.html")