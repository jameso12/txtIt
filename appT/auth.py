from crypt import methods
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import create_engine

bp = Blueprint("auth", __name__, url_prefix="/auth")

#backend logic for login
@bp.route('/login', methods = ('GET', 'POST'))
def login():
    pass
# backend logic for logout
@bp.route('/logout')
def logout():
    # end the session
    pass
# Backen logic for register page
@bp.route('/register', methods=("GET","POST"))
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if not username:
            error = "Username required"
        elif not password:
            error = "Password required"
        if error is None:
            # check to see if user already in db
            with current_app:
                db = create_engine(current_app.config['DATABASE'])
                dbSearchUser = db.execute(f"SELECT username FROM users WHERE username='{username}'").fetchone()
            if username in dbSearchUser:
                error = f'{username} already registered'
            else:
                with current_app:
                    db = create_engine(current_app.config['DATABASE'])
                    db.execute(f'INSERT INTO users(username, password) VALUES("{username}", "{password}")')
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register')

#this will load the user into g.user making sure to have a reference to the db row
@bp.before_app_request
def loadLoggedUser():
    pass
#making sure the user is logged in for operations that requiere it
def loginRequired():
    # check to see if looged in maybe g.user
    pass