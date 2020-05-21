from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/me')
def profile():
    return "Tareq Monwer"

@app.route('/blog')
def blog():
    return "My personal blog"

@app.route('/blog/<int:id>')
def article(id):
    return f"Post {id}".upper()
