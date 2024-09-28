import streamlit as st

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

# Function to display messages
def display_messages():
    for msg in st.session_state.messages:
        if msg['user'] == "user":
            st.write(f"<div style='text-align: right; margin: 5px;'><b>You:</b> {msg['message']}</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div style='text-align: left; margin: 5px;'><b>Bot:</b> {msg['message']}</div>", unsafe_allow_html=True)

# Display chat messages
display_messages()

# Chatbot options
st.write("Or select an option:")
if st.button("Recommend degrees or skills for a job position"):
    # Clear previous bot response
    if st.session_state.messages and st.session_state.messages[-1]['user'] == "bot":
        st.session_state.messages.pop()  # Remove last bot message
    st.session_state.messages.append({"user": "user", "message": "Recommend degrees or skills for a job position"})
    bot_response = "To excel in a job position, degrees in relevant fields, alongside skills like critical thinking and communication, are essential."
    st.session_state.messages.append({"user": "bot", "message": bot_response})

if st.button("Jobs I can apply for with my qualifications"):
    # Clear previous bot response
    if st.session_state.messages and st.session_state.messages[-1]['user'] == "bot":
        st.session_state.messages.pop()  # Remove last bot message
    st.session_state.messages.append({"user": "user", "message": "Jobs I can apply for with my qualifications"})
    bot_response = "Based on your qualifications, you can apply for jobs such as Data Analyst, Software Developer, or Marketing Specialist."
    st.session_state.messages.append({"user": "bot", "message": bot_response})

if st.button("Find a job quickly after graduation"):
    # Clear previous bot response
    if st.session_state.messages and st.session_state.messages[-1]['user'] == "bot":
        st.session_state.messages.pop()  # Remove last bot message
    st.session_state.messages.append({"user": "user", "message": "Find a job quickly after graduation"})
    bot_response = "To find a job quickly, consider internships, networking events, and job fairs as they can provide valuable opportunities."
    st.session_state.messages.append({"user": "bot", "message": bot_response})

if st.button("Does my school affect my employment rate?"):
    # Clear previous bot response
    if st.session_state.messages and st.session_state.messages[-1]['user'] == "bot":
        st.session_state.messages.pop()  # Remove last bot message
    st.session_state.messages.append({"user": "user", "message": "Does my school affect my employment rate?"})
    bot_response = "Yes, the reputation and resources of your school can influence your employment opportunities."
    st.session_state.messages.append({"user": "bot", "message": bot_response})

if st.button("Industries in high demand"):
    # Clear previous bot response
    if st.session_state.messages and st.session_state.messages[-1]['user'] == "bot":
        st.session_state.messages.pop()  # Remove last bot message
    st.session_state.messages.append({"user": "user", "message": "Industries in high demand"})
    bot_response = "Currently, industries such as Technology, Healthcare, and Renewable Energy are in high demand."
    st.session_state.messages.append({"user": "bot", "message": bot_response})

# Input box for user messages (below the buttons) with Send button on the right
col1, col2 = st.columns([9, 1])
with col1:
    user_input = st.text_input("Type your message here:", "")

with col2:
    if st.button("Send"):
        if user_input:
            # Append user message to session state
            st.session_state.messages.append({"user": "user", "message": user_input})
            
            # Append a placeholder bot response
            bot_response = "This is a placeholder bot response."
            st.session_state.messages.append({"user": "bot", "message": bot_response})

# Refresh chat display after sending a message
# display_messages()
