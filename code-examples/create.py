import os
from flask import Flask
# from flask import render_template, request
# from models import Passenger, Flight
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def main():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()
