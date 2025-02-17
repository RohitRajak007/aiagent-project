from crewai import LLM, Agent
from tools import tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Ensure GOOGLE_API_KEY is loaded
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Check your .env file.")

# Initialize the Gemini LLM using Google AI Studio
llm = LLM(
    model="gemini-1.5-flash",   # Ensure the model is available in Google AI Studio
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,  # Pass the API key
    api_base="https://generativelanguage.googleapis.com/v1beta"  # Explicitly use Google AI Studio endpoint
)

# Senior Researcher Agent
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",  # Fixed typo: 'Unccover' → 'Uncover'
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, eager "
        "to explore and share knowledge that could change the world."
    ),
    tools=[tool],   # Ensure `tool` is properly defined in tools.py
    llm=llm,
    allow_delegation=True
)

# Writer Agent
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging "
        "narratives that captivate and educate, bringing new discoveries "
        "to light in an accessible manner."
    ),
    tools=[tool],  # Ensure the custom tools are compatible
    llm=llm,
    allow_delegation=False
)

print("✅ Agents initialized successfully!")
