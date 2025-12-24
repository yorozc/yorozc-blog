from flask import Flask
from flask_moment import Moment
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
import os

app = Flask(__name__)
moment = Moment(app)

try:
    def _uri():
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise ConfigurationError("MONGODB_URI not set")
        return uri

    def get_client() -> MongoClient:
        return MongoClient(
            _uri(),
        )

    def get_db():
        return get_client()[os.getenv("DB")]

    def get_users_collection():
        return get_db()["COLLECTION"]
except Exception as e:
    print("Unable to make connection to DB")

from website.main.routes import main
from website.posts.routes import posts
from website.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)






