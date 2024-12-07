from datetime import timedelta
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES



db = SQLAlchemy()
DB_NAME = "database.db"
photos = UploadSet('photos', IMAGES)


def create_app():
    app = Flask(__name__, template_folder='frontend/content', static_folder='frontend/assets/img')
    """This encrypts the data for the website,
    the key is a randomly generated string used to secure
    communication between the web app and its clients"""
    app.config['SECRET_KEY'] = 'ejcmwjknewjd hwkfnewkjdwemd'
    """This is the path to the database file and how to initialize the database for the app"""
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)  # Optional: Set session lifetime

    app.config['UPLOADED_PHOTOS_DEST'] = 'website/frontend/assets/img'
    db.init_app(app)
    configure_uploads(app, photos)



    from .backend.views import views
    from .backend.auth import auth

    """The url prefix means that the routes in the views blueprint will be prefixed with /"""
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .backend.models import User, Note

    with app.app_context():
        db.create_all()
    
    """This is the login manager for the app"""
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

