import os
from flask import Flask
from models import db, Flight


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def filter():
    buggy_flights = Flight.query.filter(Flight.id <= 3).all()
    for flight in buggy_flights:
        print(flight.origin, flight.destination)


def filter_in():
    my_flights = Flight.query.filter(
        Flight.origin.in_(['Bangladesh', 'U.S.A'])
    )
    for flight in my_flights:
        print(flight.origin, flight.destination)


if __name__ == "__main__":
    with app.app_context():
        # filter()
        filter_in()