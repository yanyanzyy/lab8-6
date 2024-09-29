import streamlit as st
from chatbot.chatbot_response import *

def chatbot():
    # User Profile in the header
    col1, col2, col3 = st.columns([1, 6, 1])
    with col3:
        st.image("https://lh3.googleusercontent.com/a/ACg8ocK0_IEiBum5fdzAh439e_1u_1-aRonEW_MwD5ay17MbeZ9rlw=s64", width=64)

    # Initialize session state for chat history and selected option
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None  # Initialize selected_option

    # Display chat messages
    display_messages()

    # Display chatbot options (buttons will always remain visible)
    display_options()

    # No need to reset selected_option to None here anymore
