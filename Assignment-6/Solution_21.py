
class Countdown:
    def __init__(self, start):
        """Initialize with the starting number."""
        self.current = start

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next number in the countdown or stop iteration."""
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for number in Countdown(5):
    print(number)