import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
LLM_MODEL = "owl-alpha"
#Tested models: owl-alpha, gpt-oss-120b:free

# --- Vector store ---
CHROMA_PATH = "./chroma_db"

# --- Retrieval ---
N_RESULTS = 3

# --- Documents ---
DATA_PATH = "./data"

INITIAL_PROMPT = "You are a Chatbot that helps people with their questions on Microsoft Windows, \n" \
"You are given a few short passages from Wikipedia articles with potentially relevant information, use this information in you response, if possible, when quoting the original text, use quotation marks and state: (According a Wikipedia article)"
