from crypt import methods
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app, session
from importlib_metadata import functools
from sqlalchemy import create_engine

bp = Blueprint("auth", __name__, url_prefix="/auth")

#backend logic for login
@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
        error = None
        with current_app:
            db = create_engine(current_app.config['DATABASE'])
            userRow = db.execute(f" select * from users where username='{username}'").fetchone()
        if userRow is None: # Incorrect username
            error = "Username incorrect"
        elif password != userRow[2]: 
            error = "Password incorrect"
        
        if error is None:
        #   If the passwords match make a session
            #   clear session and asign the user id to session user_id
            session.clear()
            session['user_id'] = userRow[0]
        # If everything is succesfull, reirect to main page
            return redirect(url_for('index'))
        flash(error)

    return render_template('auth/login')
# backend logic for logout
@bp.route('/logout')
def logout():
    # end the session
    session.clear()
    return redirect(url_for('index'))
# Backen logic for register page
@bp.route('/register', methods=("GET","POST"))
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username: # making sure user not empty
            error = "Username required"
        elif not password: # making sure password not empty
            error = "Password required"
        if error is None:
            # check to see if user already in db
            with current_app:
                db = create_engine(current_app.config['DATABASE'])
                dbSearchUser = db.execute(f"SELECT username FROM users WHERE username='{username}'").fetchone() # this is a tuple
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
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        with current_app:
            db = create_engine(current_app.config['DATABASE'])
            g.user = db.execute(f"SELECT * FROM users WHERE id='{user_id}'").fetchone()

#making sure the user is logged in for operations that requiere it
def loginRequired(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view