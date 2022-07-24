from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", user=current_user)
    
@views.route('/admin/')
@login_required
def admin():
    return render_template("manage_posts.html")
    
@views.route('/admin/create_posts/', methods=['GET', 'POST'])
@login_required
def create_posts():
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('body')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, title=title, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("create_posts.html")