from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, VARCHAR

db = SQLAlchemy()


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(VARCHAR(length=30), nullable=False)
    body = db.Column(VARCHAR(length=40), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), index=True)

    def __init__(self, title, body):
        self.title = title
        self.body = body
