import streamlit as st 
import pandas as pd
from io import  BytesIO

def dataframes():
    st.title("DataFrames")
    file = st.file_uploader("Load dataframe: ", type=["csv"])
    if file is not None:
        csv = pd.read_csv(file)
        field = st.selectbox("", options= csv.columns)
        search = st.text_input("Search in DataFrame: ", "")
        if search:
            #filter_data = csv[csv.apply(lambda row: row.astype(str).str.contains(search, case=False).any(),axis=1)]
            filter_data = csv[csv.apply(lambda row: search.lower() in str(row[field]).lower(), axis=1)]
        else:
            filter_data = csv
        
        st.header("Dataframe CARS")
        st.write(f"Resultados : {len(filter_data)}")
        st.dataframe(filter_data, hide_index= True,  width= 1000, column_order=["model","car","color"], column_config={"car":"MARCA","model":"MODELO","color":"COLOR"})

        excel_buffer = BytesIO()
        filter_data.to_excel(excel_buffer, index= False, engine="openpyxl")
        excel_buffer.seek(0)

        st.download_button(label="Download Excel",
                           data=excel_buffer,file_name="dataframe_Car.xlsx",)

    else:
        st.write("Please upload a CSV file to view the DataFrame.")













