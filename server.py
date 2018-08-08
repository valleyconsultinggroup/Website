import sys, os

# Imports
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flaskext.markdown import Markdown

# Configuration
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)

# Routes
@app.route('/')
def index():
    return render_template('home.html', pages=pages)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/members/')
def members():
    return render_template('members.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/join/')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
