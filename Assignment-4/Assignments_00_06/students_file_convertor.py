import streamlit as st
import pandas as pd 
import random

st.set_page_config("Students File Convertor", layout="wide")
st.title("Students File Convertor")

names = ["Jamshed", "Jojo", "Alina", "Babar" ,"khurram", "David", "Fareed", "Faqiha", "Gulnaz", "Hammad"]

students = []
for i in range(10):
    student = {
        "ID": i,
        "Name": names[i],
        "Age": random.randint(1 , 16),
        "Grade" : random.choice(["A", "B", "C", "D" , "E" , "F"]),
        "Marks": random.randint(40 , 100),
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generated Students Data")
st.write(df)

csv_file = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download CSV file",
    csv_file,
    "students.csv",
    "text/csv",
)
st.success("CSV file downloaded successfully!")