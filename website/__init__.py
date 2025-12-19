from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)

    bootstrap = Bootstrap(app)

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/about")
    def about():
        return render_template("about.html")

    return app



