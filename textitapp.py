from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, InfoModel
 
app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# db.init_app(app)

# app = Flask(__name__)

ENV = 'dev'
# development
if ENV == 'dev': 
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jamesacer:jamesacer@localhost:5432/textit"
# production
else: 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_user = InfoModel(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return f"Done!!"

if __name__ == '__main__':
    app.run(debug=True)
