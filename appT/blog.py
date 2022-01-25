from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import create_engine
from werkzeug.exceptions import abort
from appT.auth import loginRequired

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    with current_app:
        db = create_engine(current_app.config['DATABASE'])
        posts = db.execute("SELECT posts.id, title, body, created, author_id, username FROM posts JOIN user ON posts.author_id = users.id ORDER BY dateCreated DESC").fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods = ('GET','POST'))
@loginRequired
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
                db.execute(f'INSERT INTO posts (title, body, author_id) VALUES ("{title}", "{body}", {g.user[0]}')
            redirect(url_for('blog.index'))
    return render_template("blog/create.html")

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@loginRequired
def update(id):
    post = getPost(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            with current_app:
                db = create_engine(current_app.config['DATABASE'])
                db.execute(f'UPDATE posts SET title = "{title}", body = "{body}" WHERE id = {id}' )
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@loginRequired
def delete(id):
    getPost(id)
    with current_app:
        db = create_engine(current_app.config['DATABASE'])
        db.execute(f'DELETE FROM posts WHERE id = {id}')
    return redirect(url_for('blog.index'))
# @bp.route('/create', methods = ('GET','POST'))
def getPost(id, check_author=True):
    with current_app:
        db = create_engine(current_app.config['DATABASE'])
        post = db.execute(f'SELECT posts.id, title, body, dateCreated, author_id, username FROM post JOIN user ON posts.author_id = users.id WHERE posts.id = {id}').fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post[4] != g.user[0]:
        abort(403)

    return post