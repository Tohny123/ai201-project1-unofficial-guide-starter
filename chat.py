from vectorDB import vectorDB
from config import INITIAL_PROMPT, OPENROUTER_KEY, LLM_MODEL
import requests
import json

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_KEY}",
    "Content-Type": "application/json",
}

class chatBot():
    def __init__(self):
        self.vectorDB = vectorDB()
        self.initialPrompt = {
            "role": "system",
            "content": INITIAL_PROMPT
        }

    def chat(self, history, prompt):
        #this returns a string that then gets added to "history" in the main file
        # history only stores the conversation, no system prompts
        # history is also entirely stored in main
        context = self.vectorDB.queryText(prompt) # get context from chroma
        contextPrompt = {
            "role":"system",
            "content": "Fetched Context: " + context
        }
        
        #prepare payload for the ai
        messagePayload = []
        messagePayload.append(self.initialPrompt)
        messagePayload.append(contextPrompt)
        messagePayload.extend(history)

        payload = {
            "model": LLM_MODEL,
            "messages": messagePayload,
            "temperature": 0.7
        }
        
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            timeout=30
        )


        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]
