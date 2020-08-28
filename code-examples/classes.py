class Flight:
    counter = 1

    def __init__(self, origin, destination, duration):
        # Keep track of id number. 
        self.id = Flight.counter

        # Keep track of passengers.
        self.passengers = []

        # Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f"ID: {self.id}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration}")
        print()

        print('Passengers:')
        for passenger in self.passengers:
            print(f"{passenger.name}")
    
    def delay(self, amount):
        self.duration += amount
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        passenger.flight_id = self.id


class Passenger:

    def __init__(self, name):
        self.name = name



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
