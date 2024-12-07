"""Stores the URL endpoints for website API
examples are the notes, content pages"""
from flask import Blueprint, render_template, request, flash, url_for, redirect, current_app
from flask_login import login_required, current_user
from .. import db, photos
from .models import Note, Post
from datetime import datetime
"""This is the blueprint for the website it is a way to organize the website into smaller components
and it lets the file know that routes are going to be defined in this file"""

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        new_note = Note(data=note, date=datetime.now(), user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')
    return render_template("mainview.htm", user=current_user)

@views.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        image = request.form.get('image')
        title = request.form.get('title')
        description = request.form.get('description')

        new_post = Post(title=title, 
                        image=image, 
                        description=description,
                        likes=0,
                        price=0.00,
                        date=datetime.now(),
                        user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Post Created!', category='success')
    return render_template('post.html', user=current_user)

@views.route('/new_post', methods=['POST'])
@login_required
def new_post():
    title = request.form.get('title')
    descrip = request.form.get('description')
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
        with current_app.app_context():
            filename = photos.save(file)
            new_post = Post(title=title, 
                            image=filename, 
                            description=descrip,
                            likes=0,
                            price=0.00,
                            date=datetime.now(),
                            user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post Created!', category='success')
            return redirect(url_for('views.posts'))
    return 'Invalid file type'

@views.route('/posts')
@login_required
def posts():
    return render_template('post.html', user=current_user, posts=Post.query.all())