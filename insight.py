import streamlit as st
import login
import GPT as myGPT



def insight_page():
    st.title("Feedback Page")
    userID = st.number_input("Enter ID:", value=0, step=1, help="Enter your ID")
    suggestion = myGPT.getFeedbackbyID(userID)
    st.markdown(suggestion)
    
    st.markdown('''
    <script>
        window.watsonAssistantChatOptions = {
            integrationID: "b6420beb-f8fa-4325-8f9e-3cc7dc7056d6", // The ID of this integration. 
            region: "us-south", // The region your integration is hosted in.
            serviceInstanceID: "f3f62e95-7697-4c2d-ba4a-3f27d5c6e165", // The ID of your service instance.
            onLoad: function(instance) { instance.render(); }
        };
        setTimeout(function(){
            const t=document.createElement('script');
            t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + 
                (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
            document.head.appendChild(t);
        }); 
    </script>
    ''', unsafe_allow_html=True)

    # Centered and styled "Log Out" button
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Log Out", key="log_out_button", help="Log out and return to the login page"):
        st.session_state.page = "login"
    st.markdown('</div>', unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    insight_page()