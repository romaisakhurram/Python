import random
import string

def password_generator(length , use_digits , use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))

length = "Select Password Length" 

use_digits = "Use digit"

use_special ="Include Special Characters"

if "Generate Password":
    password = password_generator(length , use_digits , use_special)
    print(f"Password Generate: {password}")

