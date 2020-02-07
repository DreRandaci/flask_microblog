from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(
            digest, size
        )

    def __repr__(self):
        return "<Username: {}, email: {}>".format(self.username, self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Post {}>".format(self.body)


class UserFollower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        UniqueConstraint("user_id", "follower_id", name="_user_follower_uc"),
    )

    def __repr__(self):
        return "<user_id {}, follower_id {}>".format(
            self.user_id, self.user_follower_id
        )


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
