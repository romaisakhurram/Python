
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

def check_age(age):
    """Check if the age is valid, raise InvalidAgeError if not."""
    if age < 18:
        raise InvalidAgeError()

try:
    age = 16 
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")