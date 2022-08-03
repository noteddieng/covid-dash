from flask import render_template
from flask import current_app as app

@app.route('/')
def home():

    return render_template(

        'index.jinja2', 
        title = 'COVID-Dashboard',
        description = 'This is a slightly longer description',
        template = 'home-template',
        body = 'This is the home page of the app.'
    )

@app.route('/about')
def about():
    return "About Page"

