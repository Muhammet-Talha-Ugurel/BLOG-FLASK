from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Post
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    post = Post.query.all()
    return render_template("index.html", user=current_user, post=post)
    
@views.route('/admin/', methods=['GET','POST'])
@login_required
def admin():
    post = Post.query.all()
    return render_template("manage_posts.html", user=current_user, post=post)
    
@views.route('/admin/create_posts/', methods=['GET', 'POST'])
@login_required
def create_posts():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        if len(body) < 1:
            flash('Note is too short!', category='error')
        else:
            new_post = Post(data=body, title=title)
            db.session.add(new_post)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("create_posts.html")

@views.route("/delete-post",methods=['POST'])
def delete_post():
    post = json.loads(request.data)
    postId = post['postId']
    post = Post.query.get(postId)
    db.session.delete(post)
    db.session.commit()
    return jsonify({})