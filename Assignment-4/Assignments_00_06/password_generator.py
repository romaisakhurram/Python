import random 
import string 

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters 

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += (
            string.punctuation
        )  
    return "".join(random.choice(characters) for _ in range(length))

try:
    length = int(input("Select password length: ")) 
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
    exit()

use_digits = ("Include numbers") 
use_special = "Include special characters"

password = generate_password(length, use_digits, use_special)  
print(f"Generated Password: `{password}`") 