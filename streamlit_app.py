import streamlit as st
import pandas as pd
st.title('💀 Machine Learning App')

st.write('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**x**')
  x = df.drop('species',axis=1)
  x

  st.write('**y**')
  y = df.species
  y
with st.expander('Data Visualization'):
  # bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')
                  
# data preparations
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('male','female'))
  bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,33.9)
  bill_depth_mm = st.slider('Bill depth (mm)',13.1,21.5,17.2)
  flipper_length_mm = st.slider("Flipper length (mm)' ,172.0,231.0,201.0)
  body_mass_g = st.slider('Body mas (g)', 2700.0, 6300.0, 4207.0)
