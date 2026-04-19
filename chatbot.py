def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "name" in user_input:
        return "I am your AI chatbot"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand"