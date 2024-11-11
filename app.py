import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Market Research Agent",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

# Display logo and title
image = Image.open("lyzr-logo.png")
st.image(image, width=150)
st.title("Market Research Agent")
st.markdown("### Welcome to the Market Research Agent!")

# Initialize the LyzrAgentAPI
client = AgentAPI(x_api_key=LYZR_API_KEY)

# Input area for new messages
user_message = st.text_input("Type your message here...")

if st.button("Start"):
        response = client.chat_with_agent(
            json_body=ChatRequest(
                user_id="harshit@lyzr.ai",
                agent_id=AGENT_ID,
                message=user_message,
                session_id="jsnsx",
            )
        )
        chat_response = response['response']
        st.markdown(chat_response)
    # Store user message in chat history


# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr Agent API and OpenAI")
