from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    recent_post = 'This is recent post from blog'
    return render_template('index.html', recent_post=recent_post)

@app.route('/me')
def profile():
    return "Tareq Monwer"

@app.route('/blog')
def blog():
    return "My personal blog"

@app.route('/blog/<int:id>')
def article(id):
    return f"Post {id}"
