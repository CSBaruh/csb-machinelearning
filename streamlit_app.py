import streamlit as st
import pandas as pd

st.title('🌐 Machine Learning App')

st.info('This app buildes a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/CSBaruh/Datas/refs/heads/main/synthetic_online_retail_data.csv')
  df
