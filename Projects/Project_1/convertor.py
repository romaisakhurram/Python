import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Convertor", layout="wide")
st.title("File Convertor & Cleaner")
st.write("It can convert CSV to Excel, Excel to CSV, and clean the data by removing duplicates and empty rows.")

files = st.file_uploader("Upload csv or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(BytesIO(file.read()))
        file.seek(0)  # Reset file pointer after reading
        try:
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(BytesIO(file.read()), engine="openpyxl")
        except ImportError as e:
            st.error(f"ImportError: {e}")
            continue
        st.subheader(f"{file.name} - Preview")
        st.dataframe(df.head())
    
        if st.checkbox(f"Remove Duplicate - {file.name}"):
            df.drop_duplicates(inplace=True)
            st.success("Duplicates Removed")
            st.dataframe(df.head())

        if st.checkbox(f"Fill Missing value - {file.name}"):
            df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
            st.success("Missing Values filled with mean")
            st.dataframe(df.head())

        selected_columns = st.multiselect(f"Select columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        if st.checkbox(f"Show chart - {file.name}") and not df.select_dtypes(include=["number"]).empty:
            st.bar_chart(df.select_dtypes(include=["number"]).iloc[:, :2])

        format_choice = st.radio(f"Convert - {file.name} to:", ["csv", "Excel"], key=file.name)

        if st.button(f"Download - {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "csv":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False, engine="openpyxl")
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")

            output.seek(0)
            st.download_button("Download files", file_name=new_name, data=output, mime=mime)

            st.success("Processing Completed")