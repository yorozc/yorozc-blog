from flask import render_template, Blueprint
from datetime import datetime
import pytz
from website.test_data.test_posts import fake_posts # testing
from website.database.db import get_blog_collection

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def index():
    coll = get_blog_collection()
    
    return render_template("index.html", posts=coll.find({}), cur_time = datetime.now())

@main.route("/about")
def about():
    my_tz = datetime.now(pytz.utc).astimezone(pytz.timezone('US/Pacific'))
    cur_time = my_tz.strftime("%I:%M %p")
    return render_template("about.html", cur_time=cur_time)

