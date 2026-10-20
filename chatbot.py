# CodeAlpha Internship Task: Basic Chatbot

def chatbot_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Welcome. How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message in ["what is your name", "your name"]:
        return "I'm CodeAlpha Chatbot, your virtual assistant."

    elif message == "help":
        return (
            "You can say hello, ask how I am, "
            "ask my name, or type bye to exit."
        )

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"

    else:
        return (
            "Sorry, I don't understand that. "
            "Type 'help' to see what I can do."
        )


def main():
    print("=" * 40)
    print("       CODEALPHA CHATBOT")
    print("=" * 40)
    print("Hello! I'm your chatbot.")
    print("Type 'help' for options or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in [
            "bye", "goodbye", "exit"
        ]:
            break


if __name__ == "__main__":
    main()