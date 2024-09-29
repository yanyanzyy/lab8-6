import streamlit as st
from chatbot.chatbot_response import *
from chatbot.commands.chatbot import chatbot
from streamlit_option_menu import option_menu
from login_streamlit import display_login_page  # Import the function

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  # Track login status

# Main app page
def show_main_app():
    st.set_page_config(page_title="DecisionFlow", layout="wide")

    with st.sidebar:
        selected = option_menu(
            menu_title="DecisionFlow",
            options=["Home", "Chatbot", "Visualisation"],
            icons=["house", "android", "clipboard-data"],
            menu_icon="app-indicator",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "fafafa"},
                "icon": {"color": "blue", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#B5C3F9"}
            }
        )

    if selected == "Home":
        st.write("Welcome to the Home Page!")
    elif selected == "Chatbot":
        chatbot()
    elif selected == "Visualisation":
        st.write("Visualisation content goes here.")

# Check login status
if not st.session_state.logged_in:
    logged_in = display_login_page()  # Call the login page function
    if logged_in:  # If login is successful
        st.session_state.logged_in = True  # Update login status
        st.rerun()
else:
    show_main_app()  # Show main app if logged in
