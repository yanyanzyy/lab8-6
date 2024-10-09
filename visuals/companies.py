import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Companies that are hiring the IT roles")

file_path = r"D:\SCHOOL\UNI\Year 1\Trimester 1\INF1102 - Programming Fundamentals\Project\Data sets\Final.csv"

if file_path is not None:
    # Read the CSV file with the correct encoding
    df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')

    # Directly use a specific column for visualization
    column_to_plot = "Company/Candidate Name"  # Replace this with your specific column name

    if df[column_to_plot].dtype == 'object':
        # Count occurrences of each category
        category_counts = df[column_to_plot].value_counts()

        # Check if category_counts is not empty
        if not category_counts.empty:
            # Multi-select to choose specific data
            selected_skills = st.multiselect(
                'Select companies to visualize',
                options=category_counts.index.tolist(),  # Provide the list of options
                default=[]  # Default to show none
            )

            # Create a bar chart for selected companies
            if st.button("Generate Bar Chart") and selected_skills:
                plt.figure(figsize=(10, 5))
                category_counts[selected_skills].plot(kind='bar')
                plt.title('Companies that are hiring the IT roles')
                plt.xlabel('Companies')
                plt.ylabel('No. of roles')
                st.pyplot(plt)
