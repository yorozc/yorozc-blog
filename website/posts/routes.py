from flask import Blueprint, request, redirect, url_for, render_template
from datetime import datetime
from test_posts import fake_posts #testing only

posts = Blueprint('posts', __name__)

# make a page to add a blog post
@posts.route("/add_blog", methods=['POST', 'GET'])
def add_blog():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]
        
        post = {'author': author,
                'title': title, 
                'content': content,
                'date_posted': datetime.now().strftime("%m-%d-%Y %I:%M%p")}
        
        fake_posts.append(post)

        return redirect(url_for('index'))

    elif request.method == "GET":

        return render_template("add_blog.html")