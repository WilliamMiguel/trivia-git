from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config
from .routes.trivia import trivia, not_found

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(trivia)
    app.register_error_handler(404, not_found)
    # LoginManager(app)
    Bootstrap(app)
    return app