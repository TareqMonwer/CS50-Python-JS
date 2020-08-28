from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(
        db.Integer, db.ForeignKey("flights.id"), nullable=False)


def main():

    # create flight
    flight1 = Flight('Dubai', 'Abu Dhabi', 300)

    # Create passenger
    passenger1 = Passenger('Tarek Monwer')
    passenger2 = Passenger('Shahed')

    # Add passenger to the flight
    flight1.add_passenger(passenger1)
    flight1.add_passenger(passenger2)

    # Display details
    flight1.print_info()


if __name__ == "__main__":
    main()
