import streamlit as st
import random

st.title("Number Guessing Game")

# Input for the guessed number
original_number = random.randint(0, 99)

guessed_number = st.number_input("Guess a number between 0 and 99", min_value=1, max_value=99)

# Button to submit the guess
if st.button("Check Guess"):
    if guessed_number < original_number:
        st.write("Your guess is too low")
    elif guessed_number > original_number:
        st.write("Your guess is too high")
    else:
        st.success("You guessed the correct number!")

        # Reset the game
        original_number = random.randint(0, 99)
        st.write("A new number has been generated. Try guessing again!")
