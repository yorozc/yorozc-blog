from flask import Blueprint, request, redirect, url_for, render_template, abort
from flask_login import login_required, current_user
from datetime import datetime
from uuid import uuid4
from website.database.db import get_blog_collection

posts = Blueprint('posts', __name__)

@posts.route("/post/<post_id>", methods=["GET"])
def post(post_id):
    coll = get_blog_collection()
    return render_template('post.html', post=coll.find_one({"blog_id": post_id}))

@login_required
@posts.route("/add_post", methods=["POST", "GET"])
def add_post():
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

        return render_template("add_post.html")
    
@login_required
@posts.route("/post/<post_id>/delete_post", methods=["POST"])
def delete_post(post_id):
    if request.method == "POST":
        # look for post via blog id and delete only one
        get_blog_collection().find_one_and_delete({"blog_id": post_id})

        return redirect(url_for("main.index"))

@login_required
@posts.route("/post/<post_id>/update_post", methods=["POST", "GET"])
def update_post(post_id):
    coll = get_blog_collection()
    if request.method == "POST":
        
        # update data
        upd_title = request.form["title"]
        upd_content = request.form["content"]
        coll.update_one({"blog_id": post_id}, 
                        {"$set": {"title": upd_title,
                                "content": upd_content}}
                            )
        
        # if post.modified_count == 0:
        #     return abort(500)
        # else:

        return redirect(url_for("main.index"))
    
    elif request.method == "GET":

        post = coll.find_one({"blog_id": post_id}) #returns dict
        title = post.get("title")
        content = post.get("content")

        return render_template("update_post.html", post_id=post_id, title=title, content=content)