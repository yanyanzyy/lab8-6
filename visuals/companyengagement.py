import streamlit as st
import pandas as pd
import plotly.express as px

# File path to your Excel file
file_path = r"C:\Users\elsia\Downloads\Group Programming\company engagement.xlsx" 

if file_path:
    df = pd.read_excel(file_path)

# Prepare data for radar chart
categories = list(df.columns)
values = df.mean().tolist()

# Print categories and values to check them
st.write("Categories:", categories)
st.write("Values:", values)

# Function to create radar chart
def create_radar_chart(categories, values):
    fig = px.line_polar(r=values, theta=categories, line_close=True)
    fig.update_traces(fill='toself')
    return fig

# Function to update chart layout with title
def add_title(fig, title):
    fig.update_layout(
        title=title,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )
        ),
        showlegend=False
    )
    return fig

# Create radar chart
fig = create_radar_chart(categories, values)

# Add title to the chart
fig = add_title(fig, "Company Engagement Radar Chart")

# Display chart
st.plotly_chart(fig)
