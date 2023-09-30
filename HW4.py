import streamlit as st
import seaborn as sns
import pandas as pd

data = pd.read_csv("world-happiness-report.csv")
#plot = sns.scatterplot(data = data, x='radius_mean', y='texture_mean')

#xbut = st.radio('X', data.columns)
#ybut = st.radio('Y', data.columns)

xbut = st.selectbox('X:', data.columns, index= 2)
ybut = st.selectbox('Y:', data.columns, index = 3)
#cbut = st.selectbox('Color by:', data.columns)

plot = sns.scatterplot(data = data, x= xbut, y=ybut)

st.pyplot(fig = plot.get_figure(),  use_container_width=True)    