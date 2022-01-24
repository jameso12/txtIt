from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import create_engine
from werkzeug.exceptions import abort
from appT.auth import login_required

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    with current_app:
        db = create_engine(current_app.config['DATABASE'])
        posts = db.execute("SELECT posts.id, title, body, created, author_id, \
            username FROM posts JOIN user ON posts.author_id = users.id ORDER BY dateCreated DESC").fetchall()
    return render_template('blog/index.html', posts=posts)

def create():
    pass

def update():
    pass

def delete():
    pass

def getPost():
    pass

