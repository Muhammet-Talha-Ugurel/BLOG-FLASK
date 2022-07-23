from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")
    
@views.route('/admin/')
def admin():
    return render_template("manage_posts.html")
    
@views.route('/admin/create_posts/')
def create_posts():
    return render_template("create_posts.html")