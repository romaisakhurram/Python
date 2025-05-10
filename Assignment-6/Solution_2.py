
#2. Using CLS
#Assignment :
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total object created are {Counter.count}")
        
obj_1 = Counter()
obj_2 = Counter()
obj_3 = Counter()
obj_4 = Counter()
obj_5 = Counter()

Counter.display_counter()