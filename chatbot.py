print(" ChatBot: Hello! I am your chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "bye":
        print(" ChatBot: Goodbye! Have a nice day ")
        break

    # Greetings
    elif user_input in ["hi", "hello", "hey"]:
        print(" ChatBot: Hello there! How can I help you?")

    # Asking name
    elif "your name" in user_input:
        print(" ChatBot: I am a simple Python chatbot ")

    # Asking about user
    elif "how are you" in user_input:
        print(" ChatBot: I'm just code, but I'm running perfectly!")

    # Help
    elif "help" in user_input:
        print(" ChatBot: You can ask me about time, date, or greetings.")

    # Time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f" ChatBot: Current time is {current_time}")

    # Date
    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        print(f" ChatBot: Today's date is {today}")

    # Default response
    else:
        print(" ChatBot: Sorry, I didn't understand that. Try asking something else.")