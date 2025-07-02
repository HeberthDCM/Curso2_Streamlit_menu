import streamlit as st 
from tables import tables as t
from charts import charts
import dataframes

if "menu" not in st.session_state:
    st.session_state.menu = "Tables"

with st.sidebar:
    st.session_state.menu= st.sidebar.selectbox("Menu", ["Inicio", "DataFrames", "Charts", "Tables"])

if st.session_state.menu == "Inicio":
    st.title("Inicio")
    st.write("Bienvenido a la aplicación de Streamlit con menú.")
    st.write("Selecciona una opción del menú en la barra lateral para comenzar.")   
elif st.session_state.menu == "DataFrames":                                    
    st.title("DataFrames")
    st.write("Esta es la página de DataFrames.")
    dataframes.dataframes()
elif st.session_state.menu == "Tables":
    st.title("Tables")
    st.write("Esta es la página de Tables.")
    t() 
elif st.session_state.menu == "Charts":
    st.title("Charts")
    st.write("Esta es la página de Charts.")


