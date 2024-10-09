import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Ensure the plotting backend is set correctly
import matplotlib
matplotlib.use('Agg')

# Title of the app
st.title("Most Commonly Required IT Competencies in the Industry")

# Corrected file path
file_path = r"D:\SCHOOL\UNI\Year 1\Trimester 1\INF1102 - Programming Fundamentals\Project\Data sets\Final.csv"

# Check if the file exists
import os
if not os.path.isfile(file_path):
    st.error(f"File not found: {file_path}")
else:
    # Read the CSV file with the correct encoding
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Adjust the encoding as needed

    # Replace 'Sub-skill' with the actual column name
    column = 'Sub-skill'  # Column for the histogram

    # Handle missing values
    df[column].fillna('Unknown', inplace=True)

    # Update sub-skills based on the DataFrame
    sub_skills = df[column].unique()
    selected_sub_skills = st.multiselect('Select Sub-skills', sub_skills, default=[])

    # Further filter the DataFrame based on selected sub-skills
    filtered_df = df[df[column].isin(selected_sub_skills)]

    # Add a button to generate the chart
    if st.button('Generate Histogram'):
        # Create a histogram
        plt.figure(figsize=(10, 6))
        plt.hist(filtered_df[column], bins=len(selected_sub_skills), edgecolor='k', alpha=0.7)

        # Add labels and title
        plt.xlabel('Sub-skill')
        plt.ylabel('Frequency')
        plt.title('Frequency of Each Sub-skill')

        # Display the plot in Streamlit
        st.pyplot(plt)
