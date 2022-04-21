import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd 
# import dataset
st.title("plot and streamlit ko mila k app bnana")
salary = pd.read_csv("ml_data_salary(4).csv")

st.write(salary.describe())
# remove unknown value:
# flight.drop(['Unnamed: 0.2','Unnamed: 0.1','Unnamed: 0','f2','f3','f10'],axis=1 ,inplace=True)
st.write(salary.head(10))
# numeric_columns =list(flight.select_dtypes(['int', 'float']).columns)





# pred = flight['prediction'].unique().tolist()
# prediction = st.selectbox('which prediction should we plot?', pred,0)
# flight = flight[flight['prediction']== prediction]
# # plotting
# st.bar_chart(flight['prediction'])
# st.line_chart(flight['prediction'])
# st.plotly_chart(flight['prediction'])

# chart_select = st.sidebar.selectbox(label ="Select the chart type",
#         options=['Scatterplots', 'Lineplots','Histogram','Boxplot'])

# if chart_select == 'Scatterplots':
#     st.sidebar.subheader('Scatterplot Setting')
#     x_values = st.sidebar.selectbox('X axis', options= numeric_columns)
#     y_values = st.sidebar.selectbox('Y axis', options =numeric_columns)
#     st.plotly_chart(flight)