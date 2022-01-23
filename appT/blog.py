from flask import Blueprint, flash, g, redirect, render_template, request, url_for

bp = Blueprint('blog', __name__)
#backend logic for login
def login():
    pass
# backend logic for logout
def logout():
    pass
# Backen logic for register page
def register():
    pass
#this will load the user into g.user making sure to have a reference to the db row
def loadLoggedUser():
    pass
#making sure the user is logged in for operations that requiere it
def loginRequired():
    pass