from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from datetime import datetime
from website.database.db import get_blog_collection

posts = Blueprint('posts', __name__)

@login_required
@posts.route("/add_blog", methods=["POST", "GET"])
def add_blog():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        
        post = {'author': author,
                'title': title, 
                'content': content,
                'date_posted': datetime.now().strftime("%m-%d-%Y %I:%M%p")
                }
        
        coll = get_blog_collection()

        coll.insert_one(post)

        return redirect(url_for("main.index"))

    elif request.method == "GET":

        return render_template("add_blog.html")
    
@login_required
@posts.route("/delete_blog", methods=["POST"])
def delete():
    pass

@login_required
@posts.route("/update_blog", methods=["POST"])
def update():
    pass