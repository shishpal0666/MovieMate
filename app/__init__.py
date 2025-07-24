
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
from mongoengine import connect

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = 'static/profile_pics'
    app.config['API_KEY'] = os.getenv('API_KEY')

    # Connect to MongoDB
    mongo_uri = os.getenv('MONGO_DB')
    connect(host=mongo_uri)

    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth_routes import auth
    from app.routes.main_routes import main
    from app.routes.movie_routes import movie

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(movie)

    return app
