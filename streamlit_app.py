import pandas as pd 
import plotly.express as px
import streamlit as st

df = pd.read_csv('reduced_chowdary.csv')

add_sidebar = st.sidebar.selectbox('Dropdown label', ('Dropdown value 1','Dropdown value 2'))

if add_sidebar == 'Dropdown value 1':
    st.write("This is for dropdown value 1. It shows a sample dataframe.")    
    st.dataframe(df)
    
if add_sidebar == 'Dropdown value 2':
    st.write("This is for dropdown value 2. It shows a plotly chart.")
    st.selectbox('Sample picker:', ['pick 1', 'pick 2'])
    
    # Create a sample DataFrame
    data = {'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'orange'],
            'sales': [20, 15, 25, 30, 20, 15],
            'city': ['NYC', 'NYC', 'NYC', 'LA', 'LA', 'LA']}
    df_bar = pd.DataFrame(data)
    fig = px.bar(df_bar, x='fruit', y='sales', color='city', barmode='group')
    st.plotly_chart(fig)