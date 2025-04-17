import random

original_number = random.randint(1, 99)
print(" Guess a number between 1 and 99!")

while True:
    guessed_number = int(input("Enter your number:"))

    if guessed_number < original_number:
        print("Your guess is too low")
    elif guessed_number > original_number:
        print("Your guess is too high")
    else:
        print("You guessed the correct number!")
        break
    