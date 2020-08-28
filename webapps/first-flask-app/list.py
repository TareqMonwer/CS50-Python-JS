import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.environ["DB_URL"])
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute(
        "SELECT origin, destination, duration FROM flights"
    ).fetchall()
    for flight in flights:
        record = f"{flight.origin} to {flight.destination}, {flight.duration} minutes."
        print(record)


if __name__ == "__main__":
    main()