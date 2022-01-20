# TODO implent the DB file here
# The DB file contains a very developed skeleton for this file
# import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext # i dont think this will be used
from sqlalchemy import create_engine

# Since db implementations have to be similar because of sqlalchemy or some python standard, it shoud be fairly easy to 
# switch to postgresql. For now I will sqlite because it has native support from python and i really want to follow along this tutorial
# and learn
def get_db():
    if 'db' not in g:
        g.db = create_engine(current_app.config['DATABASE'])
        # g.db = sqlite3.connect(
        #     current_app.config['DATABASE'],
        #     detect_types=sqlite3.PARSE_DECLTYPES
        # )
        # g.db.row_factory = sqlite3.Row

    return g.db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()

# TODO ake the schema.sql correctly
# I ton think this will be encessary though
@click.command('init-db')
@with_appcontext
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')

def init_app(app): # connecting 
    # app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command)
    init_db()


