from flask_app.app.main import bp


@bp.route("/")
def index():
    return "Hello, World from main"
