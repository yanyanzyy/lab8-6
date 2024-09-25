import pandas as pd

#Read job dataset
job_data = pd.read_excel("Pre-Processing/Final.xlsx")

#Function to filter jobs based on skills
def filter_jobs(user_skills):
    # Convert user input into a list of skills (split by commas)
    skills_list = [skill.strip().lower() for skill in user_skills.split(',')]
    
    # Filter jobs by checking if any of the user's skills match the job's required skills
    filtered_jobs = job_data[job_data['Sub-skill'].apply(lambda x: any(skill in x.lower() for skill in skills_list))]
    
    # Return the filtered job results as a dictionary
    return filtered_jobs.to_dict(orient='records')

#Trial to see if able to filter
# user_input = input("Please enter skills:")

# filter_jobs(user_input)