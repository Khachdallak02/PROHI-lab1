import streamlit as st

st.set_page_config(
    page_title="About - PROHI Dashboard",
    page_icon="👋",
)

st.sidebar.image("./assets/project-logo.jpg")

# Navigation buttons
if st.sidebar.button("🏠 Dashboard"):
    st.switch_page("Dashboard.py")
    
if st.sidebar.button("👤 About", type="primary"):
    st.switch_page("pages/About.py")

st.sidebar.markdown("---")

# Title with student name
st.write("# Khachatur Dallakyan")

st.markdown("---")

# Project summary
st.markdown("""
## DSHI Course Project Summary

During the Data Science for Health Informatics (DSHI) course, I worked on a machine learning project analyzing the Titanic dataset to predict passenger survival rates. The project involved exploratory data analysis examining survival patterns across passenger classes, gender, age groups, and family sizes.

Key findings showed that women had higher survival rates than men, first-class passengers were more likely to survive than those in lower classes, and passengers traveling with small families (2-4 members) had better survival chances than solo travelers.

For the machine learning part, I implemented and compared 10 different classification models including Decision Trees, Random Forest, SVM, K-Nearest Neighbors, and Gradient Boosting. The Gradient Boosting Classifier with 50 estimators achieved the best performance with 82.7% accuracy and an F1-score of 0.815, balancing computational efficiency with predictive performance.

The project demonstrated practical applications of data preprocessing, feature engineering, model selection, and performance evaluation in a healthcare-related context.
""")

st.markdown("---")

st.markdown("""
*This summary is based on the Titanic survival prediction analysis completed as part of Homework 3 in the DSHI course. You can find the complete analysis in the notebook at `jupyter-notebooks/DSHI_HW3_KHACHATUR_DALLAKYAN.ipynb`.*
""") 