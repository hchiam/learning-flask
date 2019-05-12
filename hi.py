# http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
# python3 -m venv venv
# . venv/bin/activate
# pip install Flask
# export FLASK_APP=hi.py
# flask run
# http://localhost:5000

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/') # http://localhost:5000
def hello_world():
    return 'Hi there!'

# example of multiple routes, HTML template, and URL->variable->HTML insert:

@app.route('/hello') # http://localhost:5000/hello
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# example of error handler sent to html page:

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404

# you can specify that parameter is an integer or subpath:

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # subpath is the rest of the path after /path/
    return 'Subpath %s' % subpath

# you can redirect routes (e.g. migrating URLS):

@app.route('/error')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'login'
