import streamlit as st
import seaborn as sns
import pandas as pd

data = pd.read_csv("/Users/edmond/Downloads/data.csv")
#plot = sns.scatterplot(data = data, x='radius_mean', y='texture_mean')

#xbut = st.radio('X', data.columns)
#ybut = st.radio('Y', data.columns)

xbut = st.selectbox('X:', data.columns)
ybut = st.selectbox('Y:', data.columns)
cbut = st.selectbox('Color by:', data.columns)

plot = sns.scatterplot(data = data, x= xbut, y=ybut, c = data[cbut])

st.pyplot(fig = plot.get_figure(), theme=None, use_container_width=True)    