from multiprocessing import set_forkserver_preload
from turtle import title
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class usersModel(db.Model):
    __tablename__ = 'users'
 
    # b.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Integer(20), nullable=False)
 
    def __init__(self, username, password):
        self.username = username
        self.password = password
 
class usersModel(db.Model):
    __tablename__ = 'posts'
 
    # b.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(), nullable=False)
    # date created column
    dateCreated = db.Column(db.Date(),nullable=False)
    # author id foreign key
    authorId = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
 
    def __init__(self, title, content, dateCreated, authorId):
        self.title = title
        self.content = content
        self.authorId = authorId
        self.dateCreated = dateCreated
