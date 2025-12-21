from flask import render_template, request, redirect, url_for, Blueprint
from datetime import datetime
from test_posts import fake_posts #testing only

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("index.html", posts=fake_posts, cur_time = datetime.now())

@main.route("/about")
def about():
    return render_template("about.html")

