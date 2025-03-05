import streamlit as st

def convert_unit(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,   # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,    # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not found"

st.title("Unit Convertor")

value = st.number_input("Enter the value to convert" , min_value=1.0 , step=1.0)

unit_from = st.selectbox("Convert from", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Convert to", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")