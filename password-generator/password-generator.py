import streamlit as st
import random
import string

def password_generator(length , use_digits , use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))

st.title("Pasword Generator")

length = st.slider("Select Password Length" , min_value=6 , max_value=16 ,value=8)

use_digits = st.checkbox("Use digit")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = password_generator(length , use_digits , use_special)
    st.write(f"Password Generate: {password}")

st.write(".............................................................................")
