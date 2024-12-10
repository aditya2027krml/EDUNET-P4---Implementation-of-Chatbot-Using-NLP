import streamlit as st
import nltk
import string
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to preprocess and clean the text data
def preprocess_text(raw_doc):
    raw_doc = raw_doc.lower()  # Convert text to lowercase
    sentence_tokens = nltk.sent_tokenize(raw_doc)
    lemmer = nltk.stem.WordNetLemmatizer()
    
    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]
    
    def LemNormalize(text):
        remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))
    
    return sentence_tokens, LemNormalize

# Chatbot Response Function using NLP (Cosine Similarity)
def response(user_response, sentence_tokens, LemNormalize):
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens + [user_response])
    vals = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = vals.argsort()[0][-1]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-1]
    if req_tfidf == 0:
        return "I am sorry, I don't understand."
    else:
        return sentence_tokens[idx]

# Streamlit UI setup
st.title("Level 2: NLP-based Chatbot")

# Set background image for the main content using custom CSS
background_image_url = 'https://i.pinimg.com/236x/db/b7/fe/dbb7fecab75ca39cf6666109393b6131.jpg'  # Replace with your image URL or use a local image
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

# File upload widget to upload a text file
uploaded_file = st.file_uploader("Upload your text file", type=["txt"])

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the file content
    raw_doc = uploaded_file.read().decode('utf-8')  # Decode file content
    sentence_tokens, LemNormalize = preprocess_text(raw_doc)
    st.write("Text file uploaded successfully. You can now ask questions based on its content.")
    
    # Display previous messages (if any)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input field for user to type their query
    if prompt := st.chat_input("Ask a question"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get response from the chatbot
        response_text = response(prompt, sentence_tokens, LemNormalize)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response_text)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        # Save chat history to CSV
        chat_df = pd.DataFrame(st.session_state.messages)
        chat_df.to_csv("chat_history.csv", index=False)

        # Provide download button for CSV file
        with open("chat_history.csv", "rb") as f:
            st.download_button(
                label="Download Chat History",
                data=f,
                file_name="chat_history.csv",
                mime="text/csv"
            )

else:
    st.write("Please upload a text file to start the conversation.")
