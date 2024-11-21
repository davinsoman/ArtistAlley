"""Stores the URL endpoints for website API
examples are the notes, content pages"""
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Note
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
    return render_template("base.html", user=current_user)