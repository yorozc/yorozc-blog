from flask import Flask

def create_app():
    app = Flask(__name__)


    @app.route("/")
    def index():
        return "<h1>Hello</h1>"
    
    @app.route("/about")
    def about():
        return "<h1>About Page</h1>"

    return app



