"""Simple CLI chat interface
"""
 


import signal
import sys
 
from config import INITIAL_PROMPT
from vectorDB import vectorDB
from chat import chatBot

EXIT_COMMANDS = {"exit", "quit", "q", ":q"}
 
 
def handle_sigint(signum, frame) -> None:
    """Cleanly close the program when Ctrl+C (SIGINT) is received."""
    print("\nGoodbye!")
    sys.exit(0)
 
 
def main() -> None:
    # close the program cleanly when Ctrl+C (SIGINT) is pressed
    signal.signal(signal.SIGINT, handle_sigint)
 
    history: list[dict] = []
 

    #initalize the llm with the appropriate context

    #initialize chatbot
    chatbot = chatBot()

    print("-" * 50)
    print("  Windows Assistant  (type 'exit' or 'quit', or press Ctrl+C to leave)")
    print("-" * 50)

    print("Ready to chat!")

    while True:
        try:
            user_input = input("\n").strip()
        except EOFError:  # Ctrl+D
            print("\nGoodbye!")
            break
 
        if not user_input:
            continue
        if user_input.lower() in EXIT_COMMANDS:
            print("Goodbye!")
            break
 
        # add the user's message to the running history
        history.append({"role": "user", "content": user_input})
 
        # call your chat function with the conversation history
        reply = chatbot.chat(history, user_input)
 
        # show the reply and remember it for context
        print(reply)
        history.append({"role": "assistant", "content": reply})
 
 
if __name__ == "__main__":
    main()