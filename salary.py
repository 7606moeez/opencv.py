import streamlit as st
import pandas as pd
import plotly.express as px 

# import dataset
st.title("salary ki base pe") # title
salary = pd.read_csv("ml_data_salary (4).csv")
st.write(salary.head())

st.subheader("columns") # columns
st.write(salary.columns)

st.subheader("described") # described
st.write(salary.describe())

years_exp = salary['YearsExperience'].unique().tolist()
YearsExperience = st.selectbox('which Years should we plot?', years_exp, 0)
# salary = salary[salary['YearsExperience']== YearsExperience]

# plotting
fig = px.scatter(salary, x= "age", y= "Salary", size='distance', color='age', hover_name='age',
                log_x= True, size_max=55, range_x=[32, 40],
                range_y= [37000,80000],animation_frame= 'YearsExperience', animation_group='Salary')
fig.update_layout(width =700)                
st.write(fig)                



