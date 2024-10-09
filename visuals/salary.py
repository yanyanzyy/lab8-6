import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Ensure the plotting backend is set correctly
import matplotlib
matplotlib.use('Agg')

# Replace 'your_file_path.csv' with the path to your file
file_path = r"D:\SCHOOL\UNI\Year 1\Trimester 1\INF1102 - Programming Fundamentals\Project\Data sets\Salary_Data_Based_country_and_race.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Replace 'Column1' and 'Column2' with the actual column names you want to compare
column1 = 'Job Title'
column2 = 'Salary'

# Convert Salary column to numeric, if necessary
df[column2] = pd.to_numeric(df[column2], errors='coerce')

# Handle missing values
df[column1].fillna('', inplace=True)
df[column2].fillna(0, inplace=True)

# Add number inputs for filtering salary range
min_salary = df[column2].min()
max_salary = df[column2].max()
min_value = st.number_input('Min Salary', min_value=min_salary, max_value=max_salary, value=min_salary)
max_value = st.number_input('Max Salary', min_value=min_salary, max_value=max_salary, value=max_salary)

# Filter the DataFrame based on the salary range
filtered_df = df[(df[column2] >= min_value) & (df[column2] <= max_value)]

# Update job titles based on the filtered DataFrame
job_titles = filtered_df[column1].unique()
selected_job_titles = st.multiselect('Select Job Titles', job_titles, default=job_titles)

# Further filter the DataFrame based on selected job titles
filtered_df = filtered_df[filtered_df[column1].isin(selected_job_titles)]

# Add a button to generate the chart
if st.button('Generate Chart'):
    # Create a horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(filtered_df[column1], filtered_df[column2], label=column2)

    # Add labels and title
    plt.xlabel('Salary')
    plt.ylabel('Job Title')
    plt.title('Salary by Job Title')
    plt.legend()

    # Save the plot to a file
    plt.savefig('plot.png')

    # Display the plot in Streamlit
    st.pyplot(plt)
