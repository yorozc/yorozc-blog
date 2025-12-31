from flask import Blueprint, request, redirect, url_for, render_template, abort
from flask_login import login_required, current_user
from datetime import datetime
from uuid import uuid4
from website.database.db import get_blog_collection

posts = Blueprint('posts', __name__)

@login_required
@posts.route("/add_blog", methods=["POST", "GET"])
def add_blog():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        id = uuid4()
        
        post = {'blog_id': str(id),
                'author': author,
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
@posts.route("/blog/<blog_id>", methods=["GET"])
def blog(blog_id):
    coll = get_blog_collection()
    blog = coll.find({"blog_id": blog_id})
    if blog:
        return render_template('blog.html', post=blog)
    else:
        abort(404)
    
@login_required
@posts.route("/delete_blog", methods=["POST"])
def delete_blog(blog_id):
    if request.method == "POST":
        print(blog_id)
        # # look for post via blog id
        # post = get_blog_collection().find({"blog_id": blog_id})
        # if post["author"] != current_user:
        #     abort(403)
        


    return redirect(url_for("main.index"))

@login_required
@posts.route("/update_blog", methods=["POST"])
def update():
    pass