import numpy as np 
import pandas as pd 
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
# web app title
st.markdown('''
# **Exploratory Data Analysis Application**
This app is Developed bt codanics youtube channel called **EDA app**
 ''')
# how to upload a file from pc
with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file =st.sidebar.file_uploader("Upload your file", type=['csv'])
    df =sns.load_dataset('titanic')
    st.sidebar.markdown("[Example of CSV fie](https://www.kaggle.com/datasets/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009?select=ArXiv_old.csv)")
# profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv =pd.read_csv(uploaded_file)
        return csv
    df =load_csv() 
    pr =ProfileReport(df, explorative =True)
    st.header('**Input DF**')
    st.write(df)
    st.write('----')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for csv file')       
    if st.button('press to use example data'):
        # example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                               columns=['age','banana','codanics', 'stream','jupyter'])
            return a 
        df = load_data()
        pr =ProfileReport(df, explorative =True)
        st.header('**Input DF**')
        st.write(df)
        st.write('----')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)    
