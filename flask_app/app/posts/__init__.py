from flask import Blueprint

bp = Blueprint("posts", __name__)


from flask_app.app.posts import routes
