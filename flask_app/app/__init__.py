from flask import Flask
from flask_app.config import Config
from flask_app.app.database import db
from flask_app.app.models.posts import *


def create_app(config_class=Config()):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    from flask_app.app.main import bp as main_bp
    from flask_app.app.posts import bp as posts_bp

    app.register_blueprint(main_bp, url_prefix="/main")
    app.register_blueprint(posts_bp, url_prefix="/posts")

    @app.route("/health/")
    def health():
        return "I am fine"

    return app
