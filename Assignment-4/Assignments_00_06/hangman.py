import random

words = [
    "python",
    "javascript",
    "hangman",
    "programming",
    "developer",
    "algorithm",
    "function",
    "variable",
    "debugging",
    "software"
]

word = random.choice(words)  # randomly chooses something from the list
guessed_letter = []
attempts = 6

print("Welcome to the Hang man")
print("-" * len(word))

while attempts > 0:
  guess = input("\n guess the letter:").lower()

  if len(guess) != 1 or not guess.isalpha():
    print("Write one alphabets only!")
    continue
  if guess in guessed_letter:
    print("This letter is already guess choose another letters:")
  guessed_letter.append(guess)

  if guess in word:
    print("correct guess!")
  else:
    attempts -= 1
    print(f"Wrong guess! You have {attempts} attempts left.")

    displayed_word = " ".join([letter if letter in guessed_letter else "_" for letter in word])
    print(displayed_word)
 
    if "_" not in displayed_word:
      print(f"Congratulations! You guessed the word: {word}")
    break
else:
    print(f"Game over! The word was: {word}")
