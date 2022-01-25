from flask import Flask
# A local data base i am using
# "postgresql://jamesacer:jamesacer@localhost:5432/test"
# Another one i will b using is the textit one
import os
# app factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='misu',
        DATABASE="postgresql://jamesacer:jamesacer@localhost:5432/textit",
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
        
    with app.app_context():
        # auth blueprint
        from . import auth
        app.register_blueprint(auth.bp)  
        # blog blueprint
        from . import blog
        app.register_blueprint(blog.bp)
        app.add_url_rule('/', endpoint='index')

    return app