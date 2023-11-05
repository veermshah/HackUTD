import streamlit as st
import csv

def login_page():
    st.title("Login Page")
    # Create a dropdown for selecting a role
    
    valid = False
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"): 
        st.session_state.page = 'insight'

def getRole():
    if 'selected_role' in st.session_state:
        return st.session_state.selected_role
    else:
        return None