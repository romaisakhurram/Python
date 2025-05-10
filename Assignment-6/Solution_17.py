
def add_greeting(self):
    def greet(self):
        return "Hello from Decorator!"
    self.greet = greet
    return self

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Ali")
print(person.greet())  