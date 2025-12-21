from flask import Flask
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

from website import routes




