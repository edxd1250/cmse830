
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import altair as alt
import plotly.express as px
iris = load_iris()
labels = iris.feature_names
targets = iris.target
print(labels)
df= pd.DataFrame(iris.data, columns = labels)
#df_form['targets'] = targets

fig = px.scatter(
	df,
	x = "sepal length (cm)",
	y = "sepal width (cm)",
	size = "petal length (cm)",
	color= "petal width (cm)"

)

st.write("""
# Iris
Visualising the correlation between sepal size and petal size
""")

st.plotly_chart(fig, theme=None, use_container_width=True)