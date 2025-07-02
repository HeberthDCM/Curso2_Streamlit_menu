import streamlit as st 
import pandas as pd 

def tables():
    st.title("Tables")
    file = st.file_uploader("Sube un archivo CSV", type=["csv"])
    if file is not None:
        csv= pd.read_csv(file)
        st.subheader("Tabla de datos")
        #drop_columns = st.multiselect("Selecciona las columnas a eliminar:", options=csv.columns.tolist())      
        drop_columns = st.multiselect("Selecciona las columnas a eliminar:", options=csv.columns)   
        limit = st.slider("Limit rows:", min_value=10, max_value=len(csv), value=10)
        if drop_columns:

            st.write(f"Mostrando las primeras {limit} filas del archivo CSV:")
        table_limit = csv.head(limit)
        table_drop = table_limit.drop(columns=drop_columns, errors='ignore')
        st.write(table_drop)

        #else:
        #    st.write("No se han eliminado columnas.")   
            

    else:
        st.write("Por favor, sube un archivo CSV para ver las tablas.")       
     
     
     
     
     
     
     
     
     
     
     
     
     
     












