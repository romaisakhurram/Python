
class Car:
    def __init__(self , brand):
      self.brand = brand

    def start(self):
       print(f"{self.brand} is starting........!")

my_car = Car("Corolla")
print(my_car.brand)
my_car.start()


      