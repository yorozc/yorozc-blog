from flask import Flask, render_template, url_for

posts = [
    {
        'author': 'Yahir Orozco',
        'title': 'Blog Post 1',
        'content': 'First blog post I have done on this site',
        'date_posted': '12/18/2025'
    },
    {
        'author': 'Yahir Orozco',
        'title': 'Blog Post 2',
        'content': 'Second blog post I have done on this site',
        'date_posted': '12/19/2025'
    }
]


def create_app():
    app = Flask(__name__)

    @app.route("/")
    @app.route("/home")
    def index():
        return render_template("index.html", posts=posts)
    
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    # make a page to add a blog post

    return app



