import streamlit as st
import pandas as pd

st.title('🌐 Machine Learning App')

st.info('This app buildes a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/CSBaruh/Datas/refs/heads/main/synthetic_online_retail_data.csv')
  df

  st.write('**X**')
  X = df.drop('category_name', axis=1)
  X

  st.write('**y**')
  y = df.product_name
  y
# order_date,product_id,category_id,category_name,product_name,quantity,price,payment_method,city,review_score,gender,age
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='product_name', y= left('order_date', 7), color = 'category_name')
