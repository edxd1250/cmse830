import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit_option_menu import option_menu





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

def set_comparison_select(variable, varname='default', title='x', xaxis_title='x', yaxis_title="Average Score", ticktext=0,tickvals=0, key=0):
    
    period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"], index=3, key= f'tab{key}per')
    col1, col2 = st.columns([5,1])
    if varname == 'default':
        title=f'{variable.title()} Averages Over Time'
        xaxis_title=variable.title()
    else:
        title=f'{varname} Averages Over Time'
        xaxis_title=varname

    with col2:
        columns = []
        if period == "Average":
            avgbut = st.toggle('Average', True, disabled=True, key=f'tab{key}avg')
            if avgbut:
                columns += ["Average"]
            G1but = st.toggle('G1', key=f'tab{key}G1')
            if G1but:
                columns += ["G1"]
            G2but = st.toggle('G2', key=f'tab{key}G2')
            if G2but:
                columns += ["G2"]
            G3but = st.toggle('G3', key=f'tab{key}G3')
            if G3but:
                columns += ["G3"]
            colorscheme = select_bar_column_pallete(columns, period)
        
        if period == "G1":
            avgbut = st.toggle('Average', key=f'tab{key}avg')
            if avgbut:
                columns += ["Average"]
            G1but = st.toggle('G1',True, disabled=True, key=f'tab{key}G1')
            if G1but:
                columns += ["G1"]
            G2but = st.toggle('G2', key=f'tab{key}G2')
            if G2but:
                columns += ["G2"]
            G3but = st.toggle('G3', key=f'tab{key}G3')
            if G3but:
                columns += ["G3"]
            colorscheme = select_bar_column_pallete(columns, period)

        if period == "G2":
            avgbut = st.toggle('Average', key=f'tab{key}avg')
            if avgbut:
                columns += ["Average"]
            G1but = st.toggle('G1', key=f'tab{key}G1')
            if G1but:
                columns += ["G1"]
            G2but = st.toggle('G2', True, disabled=True, key=f'tab{key}G2')
            if G2but:
                columns += ["G2"]
            G3but = st.toggle('G3', key=f'tab{key}G3')
            if G3but:
                columns += ["G3"]
            colorscheme = select_bar_column_pallete(columns, period)

        if period == "G3":
            avgbut = st.toggle('Average', key=f'tab{key}avg')
            if avgbut:
                columns += ["Average"]
            G1but = st.toggle('G1', key=f'tab{key}G1')
            if G1but:
                columns += ["G1"]
            G2but = st.toggle('G2', key=f'tab{key}G2')
            if G2but:
                columns += ["G2"]
            G3but = st.toggle('G3', True, disabled=True, key=f'tab{key}G3')
            if G3but:
                columns += ["G3"]
            colorscheme = select_bar_column_pallete(columns, period)
    with col1:
        averages = students.groupby(variable)[columns].mean().reset_index()
        fig = px.bar(averages, x=variable, y=columns, title= title,
            barmode='group', color_discrete_sequence= colorscheme) 
        fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title)
        fig.update_yaxes(autorangeoptions_minallowed=4)
        if ticktext != 0:
            fig.update_xaxes(ticktext=ticktext, tickvals=tickvals)
        st.plotly_chart(fig, use_container_width=True)  

def plain_dist(variable, varname='default', title=0, xaxis_title='x', yaxis_title=0, ticktext=0,tickvals=0, key=0):
    counts = students[variable].value_counts().reset_index()
    if varname == 'default':
        title=f'{variable.title()} Value Counts'
    else:
        title=f'{varname} Value Counts'
        xaxis_title=varname
    counts.columns = [counts.columns[0].title(), counts.columns[1].title()]
    fig = px.bar(counts, x=counts.columns[0], y=counts.columns[1], title=title)
    if xaxis_title != 'x':
        fig.update_layout(xaxis_title=xaxis_title)
    if yaxis_title != 0:
        fig.update_layout(yaxis_title=yaxis_title)
    if ticktext != 0:
        fig.update_xaxes(ticktext=ticktext, tickvals=tickvals)
    
    st.plotly_chart(fig, use_container_width=True) 

def pass_fail_dist(variable, varname='default', title=0, xaxis_title='x', yaxis_title=0, ticktext=0,tickvals=0, barmode='group', key=0):
    
    
    col1, col2 = st.columns([1,1])
    if varname == 'default':
        title=f'{variable.title()} Pass/Fail Rates'
    else:
        title=f'{varname} Pass/Fail Rates'
        xaxis_title=varname
    
    with col1:
        percent = st.toggle('Display Proportions Instead of Counts', False, key=f'tab{key}perc')
    with col2:
        stack = st.toggle('Display Stacked Graph', False, key=f'tab{key}stack')
        if stack == True:
            barmode = 'stack'

    if percent == True:
        counts = students.groupby(variable)[["pass"]].value_counts(normalize=True).reset_index()
        counts.columns = [counts.columns[0].title(), counts.columns[1].title(), counts.columns[2].title()]
        fig = px.bar(counts, x=counts.columns[0], y=counts.columns[2], color=counts.columns[1], title= title, barmode=barmode, color_discrete_sequence=['#D0D9CD','red'])
    else:
        counts = students.groupby(variable)[["pass"]].value_counts().reset_index()
        counts.columns = [counts.columns[0].title(), counts.columns[1].title(), counts.columns[2].title()]
        fig = px.bar(counts, x=counts.columns[0], y=counts.columns[2], color=counts.columns[1], title= title, barmode=barmode, color_discrete_sequence=['#D0D9CD','red'])
    


    if xaxis_title != 'x':
        fig.update_layout(xaxis_title=xaxis_title)
    if yaxis_title != 0:
        fig.update_layout(yaxis_title=yaxis_title)
    if ticktext != 0:
        fig.update_xaxes(ticktext=ticktext, tickvals=tickvals)
    
    st.plotly_chart(fig, use_container_width=True) 

st.header("What Affects Student Success?")


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Interactive Data Explorer", ], 
        icons=['house', 'file-bar-graph'], menu_icon="cast", default_index=0)
    selected

#"Summary" 'card-text'

if selected == "Home":
    tab1, tab2= st.tabs(["Introduction", "About this Dataset"])
    with tab1:
        st.subheader("Lets explore Student Success!")
        st.image("student.webp")
        st.markdown("Student success is a multifaceted affair combining various psychological, demographical, and social factors. The purpose of the current project is to facilitate the exploration of some of these variables in hopes that one might gain a more nuanced understanding regarding the ways in which these components influence and inform the academic acheivements of high school students.")
        st.subheader("What Defines Success?")
        st.markdown("We will define \'Success\', as a students ability to understand the material distrubuted to them throughout their time taking the course. For the purposes of this project, we will measure success using a students final grade in the respective class, with a score equal or above 10 representing \'success\' and a score below 10 representing \'failure\'. It is important to note that this method of defining student success is problematically reductionalist for multiple reasons, but due to constraints in both resoruces and understanding, this was the best metric available.")
        st.markdown("Continue reading in the \'About this Dataset\' tab to learn more about the dataset used in this project, or click around in the Interactive Data Explorer to start exploring!")
    with tab2: 
        st.subheader("About this Dataset:")
        
        st.markdown("These datasets were collected by Paulo Cortez and Alice Silva in 2006 during a study aimed at assessing student achievement in secondary school. Specifically, data was collected from a total of 788 high school students located in two public schools from the Alentejo region of Portugal, Gabriel Pereira and Mousinho da Silveira. A total of two datasets were collected, a collection of Math Scores (with 395 records) and Portuguese Scores (with 649 records) These two classes in particular were chosen due to the critical role they play in subsequential classes. For example, researchers identify physics and history as core classes that build off of the fundamental understanding of Math and Portuguese (in Portugal specifically). Thus, a student's success in their academic future, as predicted by researchers, is contingent on their understanding of these two core classes.")
        st.markdown("Continue below to view the datasets in their original states, and a description of each variable and what it represents.")
        viewdata = st.selectbox("Which dataset would you like to display?", ["None", "Math Scores Dataset", "Portuguese Scores Dataset"])
        if viewdata == "Math Scores Dataset":
            st.write(pd.read_csv("student-mat.csv"))
        if viewdata == "Portuguese Scores Dataset":
            st.write(pd.read_csv("student-por.csv"))

        d1 = pd.read_csv("student-mat.csv")
        d2 = pd.read_csv("student-por.csv")

        describe = st.selectbox("Would you like to view summary statistics of the numerical variables?", ["No", "Yes, summarize the Math dataset", "Yes, summarize the Portuguese dataset"])
        if describe == "Yes, summarize the Math dataset":
            st.write(d1.describe())
        if describe == "Yes, summarize the Portuguese dataset":
            st.write(d2.describe())

        st.subheader("Description of Variables:")
        attributes = '''
            **school** - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)\\
            **sex** - student's sex (binary: 'F' - female or 'M' - male)\\
            **age** - student's age (numeric: from 15 to 22)\\
            **address** - student's home address type (binary: 'U' - urban or 'R' - rural)\\
            **famsize** - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)\\
            **Pstatus** - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)\\
            **Medu** - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)\\
            **Fedu** - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)\\
            **Mjob** - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')\\
            **Fjob** - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')\\
            **reason** - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')\\
            **guardian** - student's guardian (nominal: 'mother', 'father' or 'other')\\
            **traveltime** - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)\\
            **studytime** - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)\\
            **failures** - number of past class failures (numeric: n if 1<=n<3, else 4)\\
            **schoolsup** - extra educational support (binary: yes or no)\\
            **famsup** - family educational support (binary: yes or no)\\
            **paid** - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)\\
            **activities** - extra-curricular activities (binary: yes or no)\\
            **nursery** - attended nursery school (binary: yes or no)\\
            **higher** - wants to take higher education (binary: yes or no)\\
            **internet** - Internet access at home (binary: yes or no)\\
            **romantic** - with a romantic relationship (binary: yes or no)\\
            **famrel** - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)\\
            **freetime** - free time after school (numeric: from 1 - very low to 5 - very high)\\
            **goout** - going out with friends (numeric: from 1 - very low to 5 - very high)\\
            **Dalc** - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)\\
            **Walc** - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)\\
            **health** - current health status (numeric: from 1 - very bad to 5 - very good)\\
            **absences** - number of school absences (numeric: from 0 to 93)\n
            These grades are related with the course subject, Math or Portuguese:\\
            **G1** - first period grade (numeric: from 0 to 20)\\
            **G2** - second period grade (numeric: from 0 to 20)\\
            **G3** - final grade (numeric: from 0 to 20, output target)\\
            '''
        st.write(attributes)

  
    

if selected == "Interactive Data Explorer":
    
    data_choice = st.selectbox("##### Choose a dataset to work with:", ["Math Scores", "Portuguese Scores"])
    if data_choice == "Math Scores":
        students = pd.read_csv("student-mat.csv")
    if data_choice == "Portuguese Scores":
        students = pd.read_csv("student-por.csv")

    students['Average'] = students[['G1', 'G2', 'G3']].mean(axis=1).round(2)
    students['pass'] = np.where(students['G3']>=10, 'pass','fail')
    tab1,tab2, tab3, tab4, tab5, tab6, tab7= st.tabs([ "Tutorial", "Demographics", "Parental information", "School information", "School performance", "Extracurriculars", "Support"])

    with tab1:
        key=1
        st.subheader("Welcome to the Interactive Data Explorer!")
        st.write("In this section there are several different ways to go about exploring the data. Click through the example below for an idea on how to interpret each graph presented. When you feel you've grasped the gist of how to use the explorer, select a dataset above and click around to learn more about each variables! The variables have been grouped into categories (as seen above) for convienence and organization purposes. Have fun exploring!")
        d1 = pd.read_csv("student-mat.csv")
        d2 = pd.read_csv("student-por.csv")
        
    
       
        st.subheader("Example:")
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key='tab1graph')
        if graphtype == 'Pass/Fail Rates by Variable':
            col1, col2 = st.columns([1,1])
            title=f'Pass/Fail Rates by Class'
            st.write("Since our target variable is student success, lets take a look at pass/fail rates by class.")
            
            d1['pass'] = np.where(d1['G3']>=10, 'pass','fail')
            d2['pass'] = np.where(d2['G3']>=10, 'pass','fail')
            data = {
            'Math': d1['pass'].value_counts(normalize=True),
            'Portugese': d2['pass'].value_counts(normalize=True)}

            counts = pd.DataFrame(data, index=['pass','fail'])

            fig = px.bar(counts.T, x=['Math','Portugese'], y=['pass','fail'], title='Percentage Pass/Fail by Class', barmode='group', color_discrete_sequence=['#A1B38E','#FF2310'])
            fig.update_layout(yaxis_title="Percentages", xaxis_title = "Class")
            with col1:
                percent = st.toggle('Display Proportions Instead of Counts', False, key=f'tab{key}perc')
            with col2:
                stack = st.toggle('Display Stacked Graph', False, key=f'tab{key}stack')
                if stack == True:
                    barmode = 'stack'
                else:
                    barmode = 'group'

            if percent == True:
                data = {
            'Math': d1['pass'].value_counts(normalize=True),
            'Portugese': d2['pass'].value_counts(normalize=True)}

                counts = pd.DataFrame(data, index=['pass','fail'])

                fig = px.bar(counts.T, x=['Math','Portugese'], y=['pass','fail'], title='Percentage Pass/Fail by Class', barmode=barmode, color_discrete_sequence=['#A1B38E','#FF2310'])
                fig.update_layout(yaxis_title="Percentages", xaxis_title = "Class")
                st.plotly_chart(fig) 
                if barmode == 'group':
                    st.write("When stacked mode is selected, we gain the ability to view pass fail rates based on the propotion in which they appear in each category. For example, in this graph we can notice an alarming trend, with about 33 percent of responants scoring a failing grade in their mathematics courses while a 15 percent fail rate exists amongst portuguese students.")
                if barmode == 'stack':
                    st.write("When viewing proportions in stacked mode, we can more easily and quickly see trends in pass fail rates when comparing category to category. For example, the red portion of the math dataset is much larger than the portuguese, indicating a larger proportion of failures in that category. This type of graph is useful when looking for trends in failure rates.")

            else:
                data = {
            'Math': d1['pass'].value_counts(),
            'Portugese': d2['pass'].value_counts()}

                counts = pd.DataFrame(data, index=['pass','fail'])

                fig = px.bar(counts.T, x=['Math','Portugese'], y=['pass','fail'], title='Percentage Pass/Fail by Class', barmode=barmode, color_discrete_sequence=['#A1B38E','#FF2310'])
                fig.update_layout(yaxis_title="Percentages", xaxis_title = "Class")
                st.plotly_chart(fig) 
                if barmode == 'group':
                    st.write("This first graph provides allows one to compare the total number of passes and failures per category. For example, we can see here that there are 265 students who passed their math classes, compared to 549 students who passed their portuguese class. This type of graph will be useful when looking to compare the total amount of passes/failures per category.")
                if barmode == 'stack':
                    st.write("When viewing pass/failure counts in stacked mode, we can compare the failure rates between categories within the context of the overall distribution. For example, while we previously noticed that math scores had a much higher failure rate than portugeses scores, we can also see here that there are much more portuguese records than their are in the math dataset.")
        if graphtype == "Comparison of Average Scores Over Time":
            period = st.selectbox("Choose a Time Period to Highlight", ["Average", "G1", "G2", "G3"], index=3, key= f'tab{key}per')
            col1, col2 = st.columns([5,1])
            title='Class Averages Over Time'

            with col2:
                columns = []
                if period == "Average":
                    avgbut = st.toggle('Average', True, disabled=True, key=f'tab{key}avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key=f'tab{key}G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key=f'tab{key}G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key=f'tab{key}G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
                
                if period == "G1":
                    avgbut = st.toggle('Average', key=f'tab{key}avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1',True, disabled=True, key=f'tab{key}G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key=f'tab{key}G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key=f'tab{key}G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G2":
                    avgbut = st.toggle('Average', key=f'tab{key}avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key=f'tab{key}G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', True, disabled=True, key=f'tab{key}G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', key=f'tab{key}G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)

                if period == "G3":
                    avgbut = st.toggle('Average', key=f'tab{key}avg')
                    if avgbut:
                        columns += ["Average"]
                    G1but = st.toggle('G1', key=f'tab{key}G1')
                    if G1but:
                        columns += ["G1"]
                    G2but = st.toggle('G2', key=f'tab{key}G2')
                    if G2but:
                        columns += ["G2"]
                    G3but = st.toggle('G3', True, disabled=True, key=f'tab{key}G3')
                    if G3but:
                        columns += ["G3"]
                    colorscheme = select_bar_column_pallete(columns, period)
            with col1:
                d1['Average'] = d1[['G1', 'G2', 'G3']].mean(axis=1).round(2)
                d2['Average'] = d2[['G1', 'G2', 'G3']].mean(axis=1).round(2)
                data = {
            'Math': d1[['G1', 'G2', 'G3', 'Average']].mean().values,
            'Portugese': d1[['G1', 'G2', 'G3', 'Average']].mean().values}
                averages = pd.DataFrame(data, index=["G1", "G2","G3","Average"])
                averages = averages.T       

                fig = px.bar(averages, x=['Math', 'Portuguese'], y=columns, title= title,
                    barmode='group', color_discrete_sequence= colorscheme) 
                fig.update_layout(xaxis_title='Class', yaxis_title='Average Score')
                fig.update_yaxes(autorangeoptions_minallowed=4)
                st.plotly_chart(fig, use_container_width=True) 
                st.write("The following graph allows you to compare student scores over time. Keeping in mind that our final \'success\' score is based on a students grade in their final period (the \'G3\' category), it can be informative to explore how scores might change over time. Using this graph, you can choose to add or subtract periods of time (including an average of all scores), to compare how scores change over time for each variable. Additionally, an option is included to choose which time period to highlight in order to assist with visualization.") 

        if graphtype == 'General Distribution of Variable':
            data = {
            'Math': len(d1),
            'Portugese': len(d2)}
        counts = pd.DataFrame(data, index=['Count'])
        title=f'Class Value Counts'



        fig = px.bar(counts.T, x=['Math','Portugese'], y='Count', title=title)
        
        st.plotly_chart(fig, use_container_width=True) 
        st.write("Finally, an option is also included to view a simple bar graph of the value counts of each variable by category. Have fun exploring!")
    with tab2: 
        key = 2
        demographics = students[["age","sex","address","famsize","G1","G2","G3","Average"]] 
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ["Age","Sex","Address Type","Family Size"])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'])
        ticktext=0
        tickvals=0
        varname = 'default'
        if data_choice == 'Age':
            variable='age'
            ticktext=[15,16,17,18,19,20,21,22]
            tickvals=[15,16,17,18,19,20,21,22]
        if data_choice == 'Sex':
            variable='sex'
            ticktext=['Female','Male']
            tickvals=['F','M']
        if data_choice == 'Address Type':
            variable='address'
            ticktext=['Rural','Urban']
            tickvals=['R','U']
        if data_choice == 'Family Size':
            variable='famsize'
            ticktext=['Greater than 3', 'Less than or Equal to 3']
            tickvals=['GT3', 'LE3']
            varname = 'Family Size'
            

        if graphtype == 'Comparison of Average Scores Over Time':
        

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals,key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)



    with tab3:
        key = 3
        parents = students[["Pstatus","Medu","Fedu","Mjob","Fjob","G1","G2","G3","Average"]] 
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ["Parent's Cohabitation Status","Mother's Education Level","Father's Education Level", "Mother's Job", "Father's Job","Primary Guardian"])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key='tab3graph')
        ticktext=0
        tickvals=0
        varname = 'default'

        if data_choice == "Parent's Cohabitation Status":
            variable = 'Pstatus'
            ticktext=['Apart', 'Together']
            tickvals=['A', 'T']
            varname = "Parent's Cohabitation Status"

        if data_choice == "Mother's Education Level":
            variable = "Medu"
            varname = "Mother's Education Level"
            ticktext=['None', 'Up to 4th Grade', 'Up to 9th Grade', 'Secondary Education', 'Higher Education']
            tickvals=[0,1,2,3,4]

        if data_choice == "Father's Education Level":
            variable = "Fedu"
            varname = "Father's Education Level"
            ticktext=['None', 'Up to 4th Grade', 'Up to 9th Grade', 'Secondary Education', 'Higher Education']
            tickvals=[0,1,2,3,4]


        if data_choice == "Mother's Job":
            variable = "Mjob" 
            varname = "Mother's Job Type"
            ticktext=['Stay at Home', 'Health Sector', 'Other', 'Service Sector', 'Education Sector']
            tickvals=['at_home', 'health', 'other','services', 'teacher']
        if data_choice =="Father's Job":
            variable = "Fjob"
            varname = "Father's Job"
            ticktext=['Stay at Home', 'Health Sector', 'Other', 'Service Sector', 'Education Sector']
            tickvals=['at_home', 'health', 'other','services', 'teacher']
        if data_choice == "Primary Guardian":
            variable = "guardian"
            varname = "Primary Guardian"
            ticktext = ['Father', 'Mother', 'Other']
            tickvals = ['father','mother','other']


        if graphtype == 'Comparison of Average Scores Over Time':
            

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
    with tab4:
        key = 4
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ['School', 'Reason for Choosing School', 'Travel Time to School from Home'])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key=f'tab{key}graph')
        
        
        ticktext=0
        tickvals=0
        varname = 'default'
        
        if data_choice =='School':
            variable = 'school'
        if data_choice =='Reason for Choosing School':
            variable = 'reason'
        if data_choice == 'Travel Time to School from Home':
            variable = 'traveltime'
            varname = "Travel Time"
            ticktext = ['Less than 15 min', '15 to 30 min', '30 min to 1 hour', 'Over 1 hour']
            tickvals = [1,2,3,4]
       # if data_choice == 'Desire for Higher Education':
       #     variable = 'higher'


        if graphtype == 'Comparison of Average Scores Over Time':
  

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)

    with tab5:
        key = 5
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ['Weekly Study Time', 'Number of Failures', 'Number of Absences'])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key=f'tab{key}graph')
        
        
        ticktext=0
        tickvals=0
        varname = 'default'
        
        if data_choice == 'Weekly Study Time':
            variable = 'studytime'
            varname = 'Weekly Study Time'
            ticktext = ['Less than 2 hours', '2 to 5 hours', '5 to 10 hours', 'More than 10 hours']
            tickvals = [1,2,3,4]
        if data_choice == 'Number of Failures':
            variable = 'failures' 
            varname = "Number of Failures"
            ticktext = ['None',1,2,'3 or More']
            tickvals = [0,1,2,3]
        if data_choice == 'Number of Absences':
            variable = 'absences'
            varname = "Number of Absences"
        


        if graphtype == 'Comparison of Average Scores Over Time':
  

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)


    with tab6:
        key = 6
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ['Activity Participation', 'Presence of a Romantic Relationship', 'Amount of Freetime', 'Time Spent with Friends', 'Workday Alcohol Consumption', 'Weekend Alcohol Consumption'])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key=f'tab{key}graph')
        
        
        ticktext=0
        tickvals=0
        varname = 'default'
        
        if data_choice == 'Activity Participation':
            variable = 'activities'
        if data_choice == 'Presence of a Romantic Relationship':
            variable = 'romantic' 
        if data_choice == 'Amount of Freetime':
            variable = 'freetime' 
        if data_choice == 'Time Spent with Friends':
            variable = 'goout'
        if data_choice == 'Workday Alcohol Consumption':
            variable = 'Dalc'
        if data_choice == 'Weekend Alcohol Consumption':
            variable = 'Walc'
        


        if graphtype == 'Comparison of Average Scores Over Time':
  

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)


    with tab7:
        key = 7
        st.subheader("Let's choose a variable to look at")
        data_choice = st.selectbox("##### Choose a variable", ['Extra Education Support', 'Family Educational Support', 'Extra Paid Classes', 'Quality of Family Relationships', 'Health'])
        graphtype = st.radio("What would you like to see?", ['Pass/Fail Rates by Variable', 'Comparison of Average Scores Over Time', 'General Distribution of Variable'], key=f'tab{key}graph')
        
        
        ticktext=0
        tickvals=0
        varname = 'default'
        
        if data_choice == 'Extra Education Support':
            variable = 'schoolsup'
        if data_choice == 'Family Educational Support':
            variable = 'famsup'
        if data_choice == 'Extra Paid Classes':
            variable = 'paid'
        if data_choice == 'Quality of Family Relationships':
            variable = 'famrel'
        if data_choice == 'Health':
            variable = 'health'
        


        if graphtype == 'Comparison of Average Scores Over Time':
  

            
            if varname != 'default':
                set_comparison_select(variable, varname = varname, ticktext=ticktext, tickvals=tickvals, key=key)
            else:
                set_comparison_select(variable, ticktext=ticktext, tickvals=tickvals, key=key)
            
        if graphtype == 'General Distribution of Variable':
            if varname != 'default':
                plain_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                plain_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
        if graphtype == 'Pass/Fail Rates by Variable':
            if varname != 'default':
                pass_fail_dist(variable, ticktext=ticktext, varname = varname, tickvals=tickvals, key=key)
            else:
                pass_fail_dist(variable, ticktext=ticktext, tickvals=tickvals, key=key)
