
class Dog:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!")

dog_1 = Dog("Buddy" , "Aidi")
dog_1.bark()