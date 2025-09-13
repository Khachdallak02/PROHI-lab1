import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

st.markdown("---")

# Input widgets
st.header("Dashboard Controls")

num_patients = st.slider('Number of patients', 10, 100, 50)

chart_type = st.selectbox('Chart type', ['Scatter Plot', 'Bar Chart', 'Line Chart'])

show_data = st.checkbox('Show raw data', value=True)

# Generate some fake data
np.random.seed(42)
data = {
    'Age': np.random.randint(20, 80, num_patients),
    'Heart_Rate': np.random.randint(60, 100, num_patients),
    'Blood_Pressure': np.random.randint(90, 140, num_patients),
    'Temperature': np.random.normal(37.0, 0.5, num_patients).round(1)
}

df = pd.DataFrame(data)

# Show data table
if show_data:
    st.subheader("Patient Data")
    st.dataframe(df)

# Make chart
st.subheader("Visualization")

if chart_type == 'Scatter Plot':
    fig = px.scatter(df, x='Age', y='Blood_Pressure', title='Age vs Blood Pressure')
elif chart_type == 'Bar Chart':
    fig = px.bar(df, x=df.index, y='Heart_Rate', title='Heart Rate by Patient')
else:
    fig = px.line(df, x='Age', y='Blood_Pressure', title='Blood Pressure vs Age')

st.plotly_chart(fig)
