import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon=":weight_lifter:", layout="centered")

st.title("BMI Calculator")

cols1 , cols2 = st.columns(2)
with cols1:
    weight = st.number_input("Enter your weight (in kg)", min_value=1.0, format="%.2f")
with cols2:
    height = st.number_input("Enter your height (in kg)", min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("This is a bmi")
    st.markdown(f"{bmi:.2f}" , unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24:
        st.success("normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("over weight")
    else:
        st.error("obsity")
else:
    st.info("Please enter a valid weight and height")