import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="File Convertor", layout="wide")
st.title("File Convertor & Cleaner")
st.write("It can convert CSV to Excel, Excel to CSV, and clean the data by removing duplicates and empty rows.")

files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = os.path.splitext(file.name)[-1].lower()

        if ext == ".csv":
            df = pd.read_csv(file)
        elif ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {ext}")
            continue

        st.write(f"***File Name:*** {file.name}")
        st.write(f"***File Size:*** {file.size/1024}")

        st.write("Preview the Head of the DataFrame")
        st.dataframe(df.head())

        st.subheader("Data cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values from {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been filled!")

            st.subheader("Select Columns to keep")
            columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            st.subheader("Data Visualization")
            if st.checkbox(f"Show visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            st.subheader("Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False , engine="openpyxl")
                    mime_type = "text/csv"
                    file_name = file.name.replace(ext, "csv")
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False , engine="openpyxl")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    file_name = file.name.replace(ext, "xlsx")
                buffer.seek(0)

                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )
    st.success("All Files Processing Completed")