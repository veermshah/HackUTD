import streamlit as st
import GPT as myGPT
import csv
from login import login_page
from insight import insight_page

# Create a Streamlit app title
st.title("Homer")

# Create a session state to manage page switching
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Check the page state and render the appropriate page
if st.session_state.page == 'login':
    login_page()  # Pass the roles list to the login_page function
else:
    insight_page()