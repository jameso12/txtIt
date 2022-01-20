from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from appT.auth import login_required
from appT.db import get_db

bp = Blueprint('blog', __name__)

def index():
    db = get_db()
    posts = db.execute(
        'SELECT id, title, body, dateCreated, author_id, username'
        ' FROM posts JOIN users ON posts.author_id = users.id'
        ' ORDER BY dateCreated DESC'
    ).fetchall()
    return render_template('postCRUD/index.html', posts=posts)

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
            db.execute(f"INSERT INTO posts (title, body, author_id) VALUES ({title}, {body}, {g.user['id']})" )
                #,(title, body, g.user['id'])
            #)
            #db.commit()
            return redirect(url_for('postCRUD.index'))

    return render_template('postCRUD/createPost.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT posts.id, title, body, dateCreated, author_id, username'
        ' FROM post JOIN user ON posts.author_id = users.id'
        f' WHERE p.id = {id}'  
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
                f'UPDATE posts SET title = {title}, body = {body}'
                f' WHERE id = {id}')
            #     ,(title, body, id)
            # )
            # db.commit()
            return redirect(url_for('postCRUD.index'))

    return render_template('postCRUD/updatePost.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute(f'DELETE FROM posts WHERE id = {id}')
    return redirect(url_for('postCRUD.index'))