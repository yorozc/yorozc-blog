from flask import Flask
from flask_moment import Moment
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from bson import ObjectId
from website.models.user import User
from website.database.db import get_users_collection
import os

app = Flask(__name__)
moment = Moment(app)
bcrypt = Bcrypt(app)

app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app) 

@login_manager.user_loader
def load_user(id):
    try:
        _id = ObjectId(id)

    except Exception:
        return None
    
    users = get_users_collection()
    doc = users.find_one({"_id": _id})
    return User(doc) if doc else None

from website.main.routes import main
from website.posts.routes import posts
from website.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)






