from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from .utils.db import db
    db.init_app(app)

    from .routes.trivia import trivia, status_401, status_404, login_manager, csrf
    app.register_blueprint(trivia)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    login_manager.init_app(app)
    csrf.init_app(app)
    # LoginManager(app)
    Bootstrap(app)
    return app