import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq model (WORKING MODEL)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
)


def get_ai_reply(user_message: str) -> str:
    """
    Generate AI reply for WhatsApp message.
    """

    if not user_message:
        return "Please send a message."

    response = llm.invoke(user_message)

    return response.content
