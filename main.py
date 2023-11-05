import streamlit as st
import listings
import login
import insight

# Create a Streamlit app title
st.title("Homer - CBRE App")

# Create a session state to manage page switching
if 'page' not in st.session_state:
    st.session_state.page = 'listings'

# Define the navigation options in the sidebar
pages = {
    'House Listings': listings,
    'Login': login,
    'Insights': insight,
}

selected_page = st.sidebar.radio("Select a Page", list(pages.keys()))

# Check the selected page and render the corresponding page
pages[selected_page].main()
