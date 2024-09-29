import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Interactive Sub-Skill Data Visualizer")

file_path = r"D:\SCHOOL\UNI\Year 1\Trimester 1\INF1102 - Programming Fundamentals\Project\Final - Final.csv"

if file_path is not None:
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Show the data types of each column
    st.write("Data types:")
    st.write(df.dtypes)

    # Choose a column for visualization
    column_to_plot = st.selectbox("Select a data type to visualize", df.columns)

    if df[column_to_plot].dtype == 'object':
        # Count occurrences of each category
        category_counts = df[column_to_plot].value_counts()

        # Check if category_counts is not empty
        if not category_counts.empty:
            # Set the range for the slider
            min_count, max_count = category_counts.min(), category_counts.max()

            # Filter based on user input using slider
            min_slider, max_slider = st.slider(
                'Select the range of counts for filtering companies',
                min_value=min_count, max_value=max_count,
                value=(min_count, max_count)
            )

            # Filter categories based on the slider
            filtered_counts = category_counts[(category_counts >= min_slider) & (category_counts <= max_slider)]

            # Multi-select to choose specific data
            selected_skills = st.multiselect(
                'Select specific data company to visualize',
                options=filtered_counts.index.tolist(),  # Provide the list of options
                default=filtered_counts.index.tolist()   # Default to show all filtered
            )

            # Create a bar chart for selected companies
            if st.button("Generate Bar Chart") and selected_skills:
                plt.figure(figsize=(10, 5))
                filtered_counts[selected_skills].plot(kind='bar')
                plt.title(f'Number of IT roles hired in {column_to_plot}')
                plt.xlabel(column_to_plot)
                plt.ylabel('Count')
                st.pyplot(plt)
