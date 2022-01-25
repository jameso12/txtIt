from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import create_engine
from werkzeug.exceptions import abort
from appT.auth import loadLoggedUser

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    with current_app:
        db = create_engine(current_app.config['DATABASE'])
        posts = db.execute("SELECT posts.id, title, body, created, author_id, \
            username FROM posts JOIN user ON posts.author_id = users.id ORDER BY dateCreated DESC").fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods = ('GET','POST'))
@loadLoggedUser
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "Title is required"
        if error is not None:
            flash(error)
        else:
            with current_app:
                db = create_engine(current_app.config['DATABASE'])
                db.execute(f'INSERT INTO post (title, body, author_id) VALUES ("{title}", "{body}", {g.user[0]}')
            redirect(url_for('blog.index'))
    return render_template("blog/create.html")

@bp.route('/update', methods = ('GET','POST'))
def update():
    return render_template("blog/update.html")

# @bp.route('/create', methods = ('GET','POST'))
def delete():
    pass
# @bp.route('/create', methods = ('GET','POST'))
def getPost():
    pass

