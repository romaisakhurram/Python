
class Engine:
    def start(self):
        """Simulates starting the engine."""
        return "Engine has started."

    def stop(self):
        """Simulates stopping the engine."""
        return "Engine has stopped."


class Car:
    def __init__(self, engine):
        """Initializes the Car with an Engine object."""
        self.engine = engine

    def start_car(self):
        """Starts the car by starting the engine."""
        return self.engine.start()

    def stop_car(self):
        """Stops the car by stopping the engine."""
        return self.engine.stop()

engine = Engine()

car = Car(engine)

print(car.start_car()) 
print(car.stop_car())   