from flask import request, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': request.args.get("username")}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }, {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
