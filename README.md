# txtIt README.md

## Why txtIt?

I decided to make this website to apply and further my knowledge on the following tools: html, css, flask, python3 and postgresql. This website is being developed on ubuntu. This webste will be based from the a [tutorial project.](https://flask.palletsprojects.com/en/2.0.x/tutorial/)

## Goals:

- [x] Figure out how to format/style this md file (make it look decent).
- [ ] Host it either on heroku or my rasberrypi 4. Preferrably heroku at first since I will probalby need to use heroku on my college course.
- [x] Use postgresql as database (for the added challenge of diverting from the most tutorials).
- [ ] Avoid searching for tutorials of anyhing similar like the flask tutorial, or tutorials that make a website that is similar to this one.

## Technologies I being used:

* HTML
* CSS
* Python3
* Flask
* Postgresql
* Jinja2

## My Journey
+ Lost in the world
+ Learning
+ Initial Layout
### Lost in the world
Psycopg2 was installed because it is the adapter that allows psqlalchemy to work with postgresql.
Flask migrate was installed(tool that helps us interact with databases and tables). (Not used for now 14/01/2021)

After following along on [askpython](https://www.askpython.com/python-modules/flask/flask-postgresql) I will divert from the tutorial and make a simpler flask without the use of the app factory, as my understandng of flask is limited and and the tutorial was not enough for me to such 
a change to the app.

Since my main goal as of now is to make the app use postgresql as a database, I will be focusing on learning about that.
I will be following along a [video](https://www.youtube.com/watch?v=w25ea_I89iM) to get my database set and running on my 
development eviroment and will als use this video to see how to deploe the final project.

Since I have seen/read many tutorials, each with their own unique way of developing this project, I will be putting everything 
concerning the pythn logic of the project in a single file (main focus is to make this project work locally). That file is txtitapp.py by
the way.

After the project works locally, I will look into how i can split the python logic into multiple files without breaking the projects;
hopefully by the time I look into giving the project a better file structure I would have enough knowledge on how to actually do so.

To make the database I came accross 2 sites that might help:
+ Gave an example and used modules that are already [installed.](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/) 
+ Serving as [docs](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_multiple_tables.htm)

I figured out how to work with a database, on python. All that is left is to start implementing the app.

### Learning
After struggling with the making simply replacing some lines of code to mkae the project work with postgresql, I decided to redo the thing
almost from scratch. I made a very simple flask app, it interacted with a postgresql and redirected to a another page(the page just said welcome). Resources that helped me throught this part:
- [g object and context manager](https://flask.palletsprojects.com/en/2.0.x/appcontext/) 
- [seesion](https://flask.palletsprojects.com/en/2.0.x/api/#flask.session)
- [database conection practice](https://github.com/jameso12/psqlFlaskSnips)
### Initial Layout
For the structure will as close as possible to the flask docs tutorial, since I am interested to learn through practice how downloading the 
the project seemed so easy and how it was deployed. Additionally, to save time I kept the html files(I did some modifications on them) so that I could:
1. get a working project faster (I plan on modifying the html files later on development)
2. use my own css file and practice styling
3. focus on making the backend of the project.
## Additional Information
References used to style this page:
- https://google.github.io/styleguide/docguide/style.html#document-layout
- [MarkDown Guide](https://www.markdownguide.org/basic-syntax/#blockquotes-1)