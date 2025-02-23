from flask_app.app.database import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            # add other fields as necessary
        }


class SubPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            # add other fields as necessary
        }
