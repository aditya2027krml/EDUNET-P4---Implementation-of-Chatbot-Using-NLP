import streamlit as st
import pickle
import json

# Load the trained model and vectorizer
with open('models/level1_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# Load intents file
with open('intents.json') as file:
    intents = json.load(file)

# Function to get response from the intents based on the predicted tag
def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return intent['responses'][0]  # Choose the first response
    return "Sorry, I don't understand."

# Set background image using custom CSS
background_image_url = 'https://i.pinimg.com/236x/69/36/bd/6936bdaeabfdd4703c947a6cb044ce34.jpg'  # Replace with your image URL or use a local image
background_css = f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# Streamlit app starts here
st.title("Level 1: Intent-based chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if user_input := st.chat_input("Ask me anything!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Process input and predict tag
    user_input_transformed = vectorizer.transform([user_input])
    predicted_tag = model.predict(user_input_transformed)[0]
    
    # Get response based on predicted tag
    response = get_response(predicted_tag)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
