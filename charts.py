import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt


def charts():
    st.title("Charts Cars")
    file = st.file_uploader("Load dataframe: ", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.subheader("Tabla de datos")
        st.dataframe(df)
        st.subheader("Gráfico de barras")
        color_count = df["color"].value_counts()
        color_count.plot(kind='bar', color='skyblue')
        plt.title("Cantidad de autos por color")
        plt.xlabel("Color")
        plt.xticks(rotation=45)
        plt.ylabel("Cantidad")
        plt.grid(axis='y')
        plt.legend() 
        st.pyplot(plt)

        ## por rango
        st.subheader("Gráfico por rango")
        plt.figure( figsize=(10, 5))
        df_filtered = df[(df["year"]> 2000) & (df["year"]< 2013)]
        year_count = df_filtered["year"].value_counts().sort_index()
        year_count.plot(kind='bar', color='lightgreen') 
        plt.title("Cantidad de autos por año (2000-2013)")
        plt.xlabel("Año")
        plt.xticks(rotation=45)
        plt.ylabel("Cantidad")
        st.pyplot(plt)

        ## pie
        st.subheader("gráficos de pastel")
        plt.figure()
        car_seleccionado = st.selectbox("Selecciones modelo", sorted(df["car"].unique()))
        df_filter = df[df["car"]==car_seleccionado]
        model_count = df_filter['model'].value_counts()
        model_count.plot(kind="pie", autopct="%d%%")
        st.pyplot(plt)

    else:
        st.warning("No se ha cargado ningun archivo")
   
   
   
   
   
   