from flask import Flask
from app.config import Config
from .routes.login import login

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(login)
    return app