import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


students = pd.read_csv("student-mat.csv")
students['Average'] = students[['G1', 'G2', 'G3']].mean(axis=1).round(2)

#define functions
def set_select_palette(series,select, max_color = 'orange', other_color = 'lightgrey'):
    sortseries = series.unique()
    sortseries.sort()
    pal = []

    for item in sortseries:
        if item == select:
            pal.append(max_color)
        else:
            pal.append(other_color)
    return pal

def select_bar_column_pallete(values, select, sel_color = 'orange', other_color = 'lightgrey'):
    pal = []
    for item in values:
        if item == select:
            pal.append(sel_color)
        else:
            pal.append(other_color)
    return pal

st.header("What Affects Student Success?")

tab2, tab3, tab4, tab5, tab6, tab7, tab1 = st.tabs(["Demographics", "Parental information", "School information", "School performance", "Extracurriculars", "Support", "Introduction"])
 
with tab2:

    demographics = students[["age","sex","address","famsize","G1","G2","G3","Average"]] 
    st.subheader("Let's choose a variable to look at")
    data_choice = st.selectbox("##### Choose a variable", ["age","sex","address","family size"])
    graphtype = st.radio("What would you like to see?", ['Comparison of Averages over time', 'General distribution of variable'])
    if graphtype == 'Comparison of Averages over time':
        period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"])

        col1, col2 = st.columns([5,1])
        if data_choice == 'age':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True)
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True)
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True)
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True)
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = demographics.groupby('age')[columns].mean().reset_index()
                fig = px.bar(averages, x='age', y=columns, title='Average Score by Age',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Age", yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True)  

        if data_choice == 'sex':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True)
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True)
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True)
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True)
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = demographics.groupby('sex')[columns].mean().reset_index()
                fig = px.bar(averages, x='sex', y=columns, title='Average Score by Sex',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Sex", yaxis_title="Average Score")
                fig.update_yaxes(range=[4, None])
                st.plotly_chart(fig, use_container_width=True)  


        if data_choice == 'address':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True)
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True)
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True)
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True)
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = demographics.groupby('address')[columns].mean().reset_index()
                fig = px.bar(averages, x='address', y=columns, title='Average Score by Address',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Address", yaxis_title="Average Score")
                fig.update_yaxes(range=[4, None])
                st.plotly_chart(fig, use_container_width=True)  
        if data_choice == 'family size':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True)
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True)
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True)
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True)
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = demographics.groupby('famsize')[columns].mean().reset_index()
                fig = px.bar(averages, x='famsize', y=columns, title='Average Score by Family Size',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Family Size", yaxis_title="Average Score")
                fig.update_yaxes(range=[4, None])
                st.plotly_chart(fig, use_container_width=True)  

    if graphtype == 'General distribution of variable':
        if data_choice == 'age':
            counts = demographics['age'].value_counts().reset_index()
            counts.columns = ['Age', 'Count']
            fig = px.bar(counts, x='Age', y='Count', title='Age Value Counts', color_discrete_sequence=['orange'])
            fig.update_layout(xaxis_title="Age", yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True)  
        if data_choice == 'sex':
            counts = demographics['sex'].value_counts().reset_index()
            counts.columns = ['Sex', 'Count']
            fig = px.bar(counts, x='Sex', y='Count', title='Sex Value Counts', color_discrete_sequence=['orange'])
            fig.update_layout(xaxis_title="Sex", yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True)
        if data_choice == 'address':
            counts = demographics['address'].value_counts().reset_index()
            counts.columns = ['Address', 'Count']
            fig = px.bar(counts, x='Address', y='Count', title='Address Value Counts', color_discrete_sequence=['orange'])
            fig.update_layout(xaxis_title="Address", yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'family size':
            counts = demographics['famsize'].value_counts().reset_index()
            counts.columns = ['Family Size', 'Count']
            fig = px.bar(counts, x='Family Size', y='Count', title='Family Size Value Counts', color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 
with tab3:
    parents = students[["Pstatus","Medu","Fedu","Mjob","Fjob","G1","G2","G3","Average"]] 
    st.subheader("Let's choose a variable to look at")
    data_choice = st.selectbox("##### Choose a variable", ["Parent's cohabitation status","Mother's education Level","Father's education Level", "Mother's Job", "Father's Job","guardian"])
    graphtype3 = st.radio("What would you like to see?", ['Comparison of Averages over time', 'General distribution of variable'], key='tab3graph')
    if graphtype3 == 'Comparison of Averages over time':
        period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"], key='tab3period')
        col1, col2 = st.columns([5,1])
        if data_choice == "Parent's cohabitation status":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('Pstatus')[columns].mean().reset_index()
                fig = px.bar(averages, x='Pstatus', y=columns, title='Average Score by Cohabitation Status',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Age", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['Apart', 'Together'], tickvals=['A', 'T'])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True)  
        if data_choice == "Mother's education Level":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

            with col1:

                averages = students.groupby('Medu')[columns].mean().reset_index()
                fig = px.bar(averages, x='Medu', y=columns, title="Average Score by Mother's education Status",
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Mother's education Level", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['None', 'Elementary', 'Middleschool', 'Highschool', "College+"], tickvals=[0,1,2,3,4])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True)  
        if data_choice == "Father's education Level":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('Fedu')[columns].mean().reset_index()
                fig = px.bar(averages, x='Fedu', y=columns, title="Average Score by Father's education status",
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Father's education Level", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['None', 'Elementary', 'Middleschool', 'Highschool', "College+"], tickvals=[0,1,2,3,4])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True)  
        if data_choice == "Mother's Job":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('Mjob')[columns].mean().reset_index()
                fig = px.bar(averages, x='Mjob', y=columns, title="Average Score by Mother's Job",
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Mother's Job", yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True)  
        if data_choice == "Father's Job":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('Fjob')[columns].mean().reset_index()
                fig = px.bar(averages, x='Fjob', y=columns, title="Average Score by Father's Job",
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Father's Job", yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 

        if data_choice == "guardian":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G2":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                if period == "G3":
                    avgbut = st.toggle('Average', key='tab3avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab3g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab3g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab3g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('guardian')[columns].mean().reset_index()
                fig = px.bar(averages, x='guardian', y=columns, title="Average Score by Guardian",
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Father's Job", yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
            
    if graphtype3 == 'General distribution of variable':

        if data_choice == "Parent's cohabitation status":
            counts = students['Pstatus'].value_counts().reset_index()
            counts.columns = ['Cohabition Status', 'Count']
            fig = px.bar(counts, x='Cohabition Status', y='Count', title='Cohabitation Status Value Counts', color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 

        if data_choice == "Mother's education Level":
            counts = students['Medu'].value_counts().reset_index()
            counts.columns = ["Mother's education Level", 'Count']
            fig = px.bar(counts, x="Mother's education Level", y='Count', title="Value Counts by Mother's Education", color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            fig.update_xaxes(ticktext=['None', 'Elementary', 'Middleschool', 'Highschool', "College+"], tickvals=[0,1,2,3,4])
            st.plotly_chart(fig, use_container_width=True)

        if data_choice == "Father's education Level":
            counts = students['Fedu'].value_counts().reset_index()
            counts.columns = ["Father's education Level", 'Count']
            fig = px.bar(counts, x="Father's education Level", y='Count', title="Value Counts by Father's Education", color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            fig.update_xaxes(ticktext=['None', 'Elementary', 'Middleschool', 'Highschool', "College+"], tickvals=[0,1,2,3,4])
            st.plotly_chart(fig, use_container_width=True)

        if data_choice == "Mother's Job":
            counts = students['Mjob'].value_counts().reset_index()
            counts.columns = ["Mother's Job", 'Count']
            fig = px.bar(counts, x="Mother's Job", y='Count', title="Value Counts by Mother's Job Type", color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True)
        if data_choice == "Father's Job":
            counts = students['Fjob'].value_counts().reset_index()
            counts.columns = ["Father's Job", 'Count']
            fig = px.bar(counts, x="Father's Job", y='Count', title="Value Counts by Father's Job Type", color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True)
        if data_choice == "guardian":
            counts = students['guardian'].value_counts().reset_index()
            counts.columns = ["Guardian", 'Count']
            fig = px.bar(counts, x="Guardian", y='Count', title="Value Counts by Guardian", color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Let's choose a variable to look at")
    data_choice = st.selectbox("##### Choose a variable", ['School', 'Reason for choosing school', 'Travel time to school from home', 'Desire for higher education (higher)'])
    graphtype = st.radio("What would you like to see?", ['Comparison of Averages over time', 'General distribution of variable'], key='tab4graph')
    if graphtype == 'Comparison of Averages over time':
        period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"], key='tab4period')
        col1, col2 = st.columns([5,1])
        if data_choice == "School":
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('school')[columns].mean().reset_index()
                fig = px.bar(averages, x='school', y=columns, title='Average Score by School',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="School", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['Gabriel Pereira', 'Mousinho da Silveira'], tickvals=['GP','MS'])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
        
        if data_choice == 'Reason for choosing school':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('reason')[columns].mean().reset_index()
                fig = px.bar(averages, x='reason', y=columns, title='Average Score by Reason',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Reason", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['Course Preference', 'Close to Home', 'Other', 'Reputation'], tickvals=[0,1,2,3])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'Travel time to school from home':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('traveltime')[columns].mean().reset_index()
                fig = px.bar(averages, x='traveltime', y=columns, title='Average Score by Travel Time',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Travel Time", yaxis_title="Average Score")
                fig.update_xaxes(ticktext=['<15 min', '15 to 30 min', '30 min. to 1 hour', '>1 hour'], tickvals=[1,2,3,4])
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'Desire for higher education (higher)':
            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab4avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab4g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab4g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab4g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('higher')[columns].mean().reset_index()
                fig = px.bar(averages, x='higher', y=columns, title='Average Score by Desire for Higher Education',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title="Desire", yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 

    if graphtype == 'General distribution of variable':
        if data_choice == "School":
            counts = students['school'].value_counts().reset_index()
            counts.columns = ['School', 'Count']
            fig = px.bar(counts, x='School', y='Count', title='Value Counts by School', color_discrete_sequence=['orange'])
            fig.update_xaxes(ticktext=['Course Preference', 'Close to Home', 'Other', 'Reputation'], tickvals=[0,1,2,3])
            fig.update_layout(yaxis_title="Number of Individuals")
            

            st.plotly_chart(fig, use_container_width=True) 

        if data_choice == 'Reason for choosing school':
            counts = students['reason'].value_counts().reset_index()
            counts.columns = ['Reason', 'Count']
            fig = px.bar(counts, x='Reason', y='Count', title='Value Counts by Reason', color_discrete_sequence=['orange'])
            fig.update_layout(yaxis_title="Number of Individuals")
            fig.update_xaxes(ticktext=['Course Preference', 'Close to Home', 'Other', 'Reputation'], tickvals=[0,1,2,3])
            st.plotly_chart(fig, use_container_width=True) 

        if data_choice == 'Travel time to school from home':
            counts = students['traveltime'].value_counts().reset_index()
            fig = px.bar(counts, x=counts.iloc[:,0], y=counts.iloc[:,1], title=f'Value Counts by {data_choice}', color_discrete_sequence=['orange'])
            fig.update_layout(xaxis_title=data_choice, yaxis_title="Number of Individuals")
            fig.update_xaxes(ticktext=['<15 min', '15 to 30 min', '30 min. to 1 hour', '>1 hour'], tickvals=[1,2,3,4])
            st.plotly_chart(fig, use_container_width=True) 

        if data_choice == 'Desire for higher education (higher)':
            counts = students['higher'].value_counts().reset_index()
            fig = px.bar(counts, x=counts.iloc[:,0], y=counts.iloc[:,1], title=f'Value Counts by {data_choice}', color_discrete_sequence=['orange'])
            fig.update_layout()
            fig.update_layout(xaxis_title=data_choice, yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 

with tab5:
    st.subheader("Let's choose a variable to look at")
    data_choice = st.selectbox("##### Choose a variable", ['Weekly Study Time', 'Number of Failures', 'Number of Absences'])
    graphtype = st.radio("What would you like to see?", ['Comparison of Averages over time', 'General distribution of variable'], key='tab5graph')
    if graphtype == 'Comparison of Averages over time':
        period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"], key='tab5period')
        col1, col2 = st.columns([5,1])
        if data_choice == 'Weekly Study Time':
            with col2:    
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('studytime')[columns].mean().reset_index()
                fig = px.bar(averages, x=averages.iloc[:,0], y=columns, title=f'Average Score by {data_choice}',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title=data_choice, yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 

        if data_choice == 'Number of Failures':
            with col2:    
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('failures')[columns].mean().reset_index()
                fig = px.bar(averages, x=averages.iloc[:,0], y=columns, title=f'Average Score by {data_choice}',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title=data_choice, yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'Number of Absences':
            with col2:    
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key='tab5avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key='tab5g1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key='tab5g2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key='tab5g3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                averages = students.groupby('absences')[columns].mean().reset_index()
                fig = px.bar(averages, x=averages.iloc[:,0], y=columns, title=f'Average Score by {data_choice}',
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title=data_choice, yaxis_title="Average Score")
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 

    if graphtype == 'General distribution of variable':
        if data_choice == 'Weekly Study Time':
            counts = students['studytime'].value_counts().reset_index()
            fig = px.bar(counts, x=counts.iloc[:,0], y=counts.iloc[:,1], title=f'Value Counts by {data_choice}', color_discrete_sequence=['orange'])
            fig.update_layout()
            fig.update_layout(xaxis_title=data_choice, yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'Number of Failures':
            counts = students['failures'].value_counts().reset_index()
            fig = px.bar(counts, x=counts.iloc[:,0], y=counts.iloc[:,1], title=f'Value Counts by {data_choice}', color_discrete_sequence=['orange'])
            fig.update_layout()
            fig.update_layout(xaxis_title=data_choice, yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 
        if data_choice == 'Number of Absences':
            counts = students['absences'].value_counts().reset_index()
            fig = px.bar(counts, x=counts.iloc[:,0], y=counts.iloc[:,1], title=f'Value Counts by {data_choice}', color_discrete_sequence=['orange'])
            fig.update_layout()
            fig.update_layout(xaxis_title=data_choice, yaxis_title="Number of Individuals")
            st.plotly_chart(fig, use_container_width=True) 

with tab1:
    st.subheader("Intro work in progress...")
    data_choice = st.selectbox("##### Choose a dataset", students.columns)

    fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3, figsize=(14,4), sharey = True)

    sns.countplot(x=students['G1'], ax=ax1, palette=set_select_palette(students['G1'],0))
    sns.countplot(x=students['G2'],ax=ax2 ,palette=set_select_palette(students['G2'],0))

    sns.countplot(x=students['G3'], ax=ax3, palette=set_select_palette(students['G3'],0))
    #g2 without zeros
    g2_0 = students.loc[students['G2']==0]
    g2_no0 = students.loc[students['G2']!=0]
    g2_no0['G2'].mean()
    #g3 without zeros
    g3_0 = students.loc[students['G3']==0]
    g3_no0 = students.loc[students['G3']!=0]
    g3_no0['G3'].mean()


    avg_data = pd.DataFrame({'Dataset': ['G1', 'G1','G2','G2','G3','G3'], 'Zeros':['with','without','with','without','with','without'], 'Average': [students['G1'].mean(),0,students['G2'].mean(),g2_no0['G2'].mean(),students['G3'].mean(), g3_no0['G3'].mean()]})
    #barplot w/without zeros
    fig2 = px.bar(avg_data, x='Dataset', y='Average', title='With Zeroes vs Without',
                barmode='group', color='Zeros', color_discrete_sequence= set_select_palette(avg_data['Zeros'],'without', max_color = 'orange'))  # Set barmode to 'group' for grouped bars

    # Customize the layout (optional)
    fig2.update_layout(xaxis_title="Dataset", yaxis_title="Average Value", width=800, height=500)

    # Show the plot
    st.plotly_chart(fig2) 