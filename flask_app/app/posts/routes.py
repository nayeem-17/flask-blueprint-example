from flask_app.app.models.posts import Post, SubPost
from flask_app.app.posts import bp
from flask import jsonify


@bp.route("/")
def index():
    return "Hello, World from posts"


# get all the posts and send it to the client
@bp.route("/all/")
def get_all_posts():
    posts = Post.query.all()
    posts_list = [post.to_dict() for post in posts]
    return jsonify(posts_list)


# get all the posts and send it to the client
@bp.route("/all/sp")
def get_all_posts_sp():
    posts = SubPost.query.all()
    posts_list = [post.to_dict() for post in posts]
    return jsonify(posts_list)
