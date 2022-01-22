from operator import index
from flask import Flask, render_template, g, request, redirect, url_for, session
from sqlalchemy import create_engine

from flask import Flask
# A local data base i am using
# "postgresql://jamesacer:jamesacer@localhost:5432/test"
# Another one i will b using is the textit one
import os
# app factory
def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'misu'
    @app.route('/', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'

            if error is None:
                session.pop('user', None)
                session['user'] = username
                with app.app_context():
                    g.db = create_engine("postgresql://jamesacer:jamesacer@localhost:5432/test")
                    g.db.execute(f"INSERT INTO om (username, password) VALUES ('{username}', '{password}')")

                return redirect(url_for("protected"))

        return render_template('auth/register.html')

    @app.route('/protected')
    def protected():
        return render_template('imp.html')
    
            
    return app
