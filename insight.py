import streamlit as st
import login
import GPT as myGPT



def insight_page():
    st.title("Feedback Page")
    userID = st.number_input("Enter ID:", value=0, step=1, help="Enter your ID")
    suggestion = myGPT.getFeedbackbyID(userID)
    st.write(suggestion)

   
    # Centered and styled "Log Out" button
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Log Out", key="log_out_button", help="Log out and return to the login page"):
        st.session_state.page = "login"
    st.markdown('</div>', unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    insight_page()