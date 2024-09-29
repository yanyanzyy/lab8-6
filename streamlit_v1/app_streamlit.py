import streamlit as st
from chatbot.chatbot_response import *
from chatbot.commands.chatbot import chatbot
from streamlit_option_menu import option_menu



# Setting up the layout of the app
st.set_page_config(page_title="DecisionFlow", layout="wide")

# Sidebar for the chatbot with a bigger button
# st.sidebar.title("DecisionFlow")
# st.sidebar.markdown("<a href='#' style='display: block; text-align: center; padding: 10px; background-color: #B5C3F9; border-radius: 5px; font-size: 1.25rem; color: white; text-decoration: none;'>Chatbot</a>", unsafe_allow_html=True)

with st.sidebar:
    selected=option_menu(
        menu_title="DecisionFlow",
        options= ["Home", "Chatbot", "Visualisation"],
        icons = ["house", "android", "clipboard-data"],
        menu_icon=["app-indicator"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "fafafa"},
            "icon": {"color": "blue", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#B5C3F9"}
        }
    )

if selected == "Home":
    pass
if selected == "Chatbot":
    chatbot()

if selected == "Visualisation":
    pass
