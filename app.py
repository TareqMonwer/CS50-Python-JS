from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    categories = ['Learning English', 'Python', 'Django']
    recent_post = 'This is recent post from blog'
    return render_template('index.html',
        recent_post=recent_post, categories=categories)

@app.route('/me')
def about():
    categories = ['Learning English', 'Python', 'Django']
    return render_template('me.html', categories=categories)

@app.route('/blog')
def blog():
    return "My personal blog"

@app.route('/blog/<int:id>')
def article(id):
    return f"Post {id}"
