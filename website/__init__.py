from flask import Flask, render_template, url_for, request, redirect
from flask_moment import Moment
from datetime import datetime

posts = [
    {
        'author': 'Yahir Orozco',
        'title': 'Blog Post 1',
        'content': 'First blog post I have done on this site',
        'date_posted': datetime.now().strftime("%m-%d-%Y %I:%M%p")
    },
    {
        'author': 'Yahir Orozco',
        'title': 'Blog Post 2',
        'content': 'Second blog post I have done on this site',
        'date_posted': datetime.now().strftime("%m-%d-%Y %I:%M%p")
    }
]


def create_app():
    app = Flask(__name__)
    moment = Moment(app)
    

    @app.route("/")
    @app.route("/home")
    def index():
        return render_template("index.html", posts=posts, cur_time = datetime.now())
    
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    # make a page to add a blog post
    @app.route("/add_blog", methods=['POST', 'GET'])
    def add_blog():
        if request.method == "POST":
            author = request.form["author"]
            print(author)

            return redirect(url_for('index'))

        elif request.method == "GET":
            return render_template("add_blog.html")

    return app



