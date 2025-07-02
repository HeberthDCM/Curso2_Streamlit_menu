import streamlit as st 

def charts():
    st.title("Charts")
    st.write("This is the Charts page.")
    
    # Example chart using Streamlit's built-in chart function
    data = [1, 2, 3, 4, 5]
    st.line_chart(data)  # Display a simple line chart in Streamlit
    
    # You can add more complex charts using libraries like Matplotlib or Plotly if needed