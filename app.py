import streamlit as st
import seaborn as sns
import pandas as pd

header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("kashti ki app")
    st.text("In the project we will on kashti data")

with data_sets:
    st.header("kashti dhoob gayi")
    st.text("we will work on titanic datasets")
    df = sns.load_dataset('titanic')
    st.write(df.head())




with features:
    st.header("these are our app features")
    st.text("input data ")

with model_training:
    st.header("kya bna kashti walo ka")       