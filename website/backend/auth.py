from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note, Post
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Accessing the data sent on this route from the form"""
    data = request.form
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in successfully!', category='success')
            remember = 'remember_me' in request.form
            """This is how you log in a user, remember is a boolean that will remember the user's session"""
            login_user(user, remember=remember)
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect email or password, try again.', category='error')
    else:
        flash('User does not exist.', category='error')
    

    """If you want to pass variables to the template you can do so by passing them as keyword arguments"""
    return render_template("login.html", title=True, user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(email)
        print(username)
        print(password)

        new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))

        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        login_user(new_user, remember=True)

        return redirect(url_for('views.home'))

        
        
    return render_template("/login.htm")

@auth.route('/home')
@login_required
def home():
    if current_user.is_authenticated:
        return render_template("mainview.htm", user=current_user)
    else:
        return redirect(url_for('auth.login'))
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted!', 'success')
    else:
        flash('Note not found', 'error')

    return redirect(url_for('views.home'))

@auth.route('/delete-post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post and post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted!', 'success')
    else:
        flash('Post not found', 'error')

    return redirect(url_for('views.home'))