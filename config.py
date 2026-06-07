import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
LLM_MODEL = "gpt-oss-120b:free"
#Tested models: owl-alpha

# --- Vector store ---
CHROMA_PATH = "./chroma_db"

# --- Retrieval ---
N_RESULTS = 3

# --- Documents ---
DATA_PATH = "./data"

INITIAL_PROMPT = "You are a Chatbot that helps people with their questions on Microsoft Windows, \n" \
"You are given a few short passages from Wikipedia articles with potentially relevant information, use this information in you response, but do not mention that you have been given this text"
