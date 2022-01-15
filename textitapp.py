from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, InfoModel
from multiprocessing import set_forkserver_preload
from turtle import title
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# db.init_app(app)

# app = Flask(__name__)

ENV = 'dev'
# development
if ENV == 'dev': 
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jamesacer:jamesacer@localhost:5432/textit"
# production
else: 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
################################        database models         ###########################################################
from sqlalchemy import create_engine

db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"

db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

# Read
result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

# Delete
db.execute("DELETE FROM films WHERE year='2016'")  
class usersModel(db.Model):
    __tablename__ = 'users'
 
    # b.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Integer(20), nullable=False)
 
    def __init__(self, username, password):
        self.username = username
        self.password = password
 
class postsModel(db.Model):
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
################################        end of database models         ###########################################################

################################        appp logic        ###########################################################

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')



@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
# The function bellow takes an argument id, which is an Int in this case. Flask will use the
# value at the id location of the url, that is why we must specify that id is an int in the 
# url (otherwise a string would be returned).

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
################################        end of app logic        ###########################################################
if __name__ == '__main__':
    app.run(debug=True)
