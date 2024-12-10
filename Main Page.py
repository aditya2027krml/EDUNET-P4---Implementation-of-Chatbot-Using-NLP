import streamlit as st

# Apply Custom CSS for Sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f4f4f4;  /* Light grey background */
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content h2 {
        color: #333;  /* Dark grey text for header */
        font-weight: bold;
    }
    .sidebar .sidebar-content a {
        font-size: 18px;  /* Increase link font size */
        color: #0073e6;  /* Blue color for links */
        font-weight: bold;
        text-decoration: none;
    }
    .sidebar .sidebar-content a:hover {
        color: #ff5733;  /* Change link color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Page Content
st.image(
    "Welcome to my CHATBOT (1).png",
    caption="Welcome to the NLP Chatbot App!",
    use_column_width=True,
)

st.title("🤖 **Chatbot using NLP & Python**")
st.markdown("---")

st.markdown(
    """
    ### 👋 Hello and Welcome!  
    This app provides an interactive experience through two chatbot levels:
    1. **🌟 Level 1**: Intent-based chatbot using a predefined intents file.
    2. **✨ Level 2**: NLP-based chatbot with a custom dataset.
    """
)

st.markdown(
    """
    🧠 **Why use this app?**
    - Simulates natural language conversations.
    - Supports both predefined and custom datasets for chatbot training.  
    
    🎯 **Get Started**
    - Select a page from the sidebar to start interacting with the chatbot. 
    - Experience the magic of AI-powered communication!
    """
)

st.markdown("---")
st.markdown("💬 *Happy Chatting!*")
