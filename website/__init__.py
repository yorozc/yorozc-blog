from flask import Flask
from flask_moment import Moment
from flask_bcrypt import Bcrypt

app = Flask(__name__)
moment = Moment(app)
bcrypt = Bcrypt(app)

from website.main.routes import main
from website.posts.routes import posts
from website.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)






