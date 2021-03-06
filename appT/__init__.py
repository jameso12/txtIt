from flask import Flask, render_template, g, url_for, request, redirect, session

import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # set secret key and connect to db
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE="postgresql://jamesacer:jamesacer@localhost:5432/test",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello') # for some reason changing from /hello to just / solved the 404 error
    def hello():
        return 'Hello, World!'
    
    # import the db to the actual app
    from . import db
    db.init_app(app)
    # import the auth routes into the actual app
    from . import auth
    app.register_blueprint(auth.bp)
    # importing the blog(heart of this project) into the actual app
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    # return instance of this app
    return app
