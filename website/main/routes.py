from flask import render_template, Blueprint
from datetime import datetime
from website.test_data.test_posts import fake_posts # testing

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("index.html", posts=fake_posts, cur_time = datetime.now())

@main.route("/about")
def about():
    return render_template("about.html")

