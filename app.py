from flask import Flask, render_template, request
from flask_session import Session


## App configs
app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Global data with session
categories = ['Learning English', 'Python', 'Django']

## Rotes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form.get('category')
        categories.append(category)

    recent_post = 'This is recent post from blog'
    return render_template('index.html',
        recent_post=recent_post, categories=categories)


@app.route('/me', methods=['GET','POST'])
def about():
    # Form data
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('email')
        text = request.form.get('message')
        return f'{name} {mail} {text}'
    return render_template('me.html', categories=categories)


@app.route('/blog')
def blog():
    return "My personal blog"


@app.route('/blog/<int:id>')
def article(id):
    return f"Post {id}"
