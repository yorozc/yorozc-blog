from flask import Flask
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

from website import routes




