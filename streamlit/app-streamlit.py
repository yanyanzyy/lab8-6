import streamlit as st
from chatbot_response import *

# Setting up the layout of the app
st.set_page_config(page_title="DecisionFlow", layout="wide")

# Sidebar for the chatbot with a bigger button
st.sidebar.title("DecisionFlow")
st.sidebar.markdown("<a href='#' style='display: block; text-align: center; padding: 10px; background-color: #B5C3F9; border-radius: 5px; font-size: 1.25rem; color: white; text-decoration: none;'>Chatbot</a>", unsafe_allow_html=True)

# User Profile in the header
col1, col2, col3 = st.columns([1, 6, 1])
with col3:
    st.image("https://lh3.googleusercontent.com/a/ACg8ocK0_IEiBum5fdzAh439e_1u_1-aRonEW_MwD5ay17MbeZ9rlw=s64", width=64)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
    
# Function to display messages
def display_messages():
    for msg in st.session_state.messages:
        if msg['user'] == "user":
            st.write(f"<div style='text-align: right; margin: 5px;'><b>You:</b> {msg['message']}</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div style='text-align: left; margin: 5px;'><b>Bot:</b> {msg['message']}</div>", unsafe_allow_html=True)

# Display chat messages
display_messages()
if st.session_state.selected_option:
    handle_option(st.session_state.selected_option)
else:
    display_options()
# user_input = st.chat_input("Type your message here:")
