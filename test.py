import streamlit as st
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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
    df = df.dropna()
    st.write(df.head(10))
    st.subheader("sex ka bar chart")
    st.bar_chart(df['sex'].value_counts())

    st.subheader("different classes")
    st.bar_chart(df['age'].sample(10))


with features:
    st.header("These are our app features:")
    st.text("input data ")
    st.markdown('1. **Feature 1:** This will tell us')    


with model_training:
    st.header("kya bna kashti walo ka?-Model training")      

    input, display = st.columns(2)

    max_depth = st.slider("How many people do you know?", min_value=10, max_value=100, value=20, step=5) 
    
n_estimators = input.selectbox('how many tree should b there in RF?', options =[50,100,200,300, 'No limits'])

# adding list of features:
input.write(df.columns)
input_features = input.text_input('which features we should use?') 


# machine learning model
model = RandomForestRegressor(max_depth = max_depth, n_estimators = n_estimators)

# hum aik model lagaye jo NO limits ko show kre ga:
if n_estimators == 'No limits':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)    
    # define X and y
X = df[[input_features]]   
y = df[['fare']]

model.fit(X, y)
pred = model.predict(y)

# Display columns:
display.subheader("Mean absolute error of the model is: ")
display.write(mean_absolute_error(y, pred))
display.subheader("Mean Squared Error of the model is: ")
display.write(mean_squared_error(y, pred))
display.subheader("R squared is: ")
display.write(r2_score(y, pred))



# st.bar_chart(df['fare'])


# st.line_chart(df['fare'])