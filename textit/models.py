from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
# ?? make the 2 table models here?
class usersModel(db.Model):
    __tablename__ = 'users'
 
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.Integer(), nullable=False)
 
    def __init__(self, username, password):
        self.username = username
        self.password = password
 
    def __repr__(self):
        return f"{self.username}"

# copy model layout for convinience
# class usersModel(db.Model):
#     __tablename__ = 'users'
 
#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(), nullable=False)
#     password = db.Column(db.Integer(), nullable=False)
 
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
 
#     def __repr__(self):
#         return f"{self.username}"