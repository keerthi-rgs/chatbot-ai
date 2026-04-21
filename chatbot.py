def get_response(message):
    msg = message.lower()

    if "hi" in msg or "hello" in msg:
        return "Hello! How can I help you?"

    elif "doctor" in msg:
        return "We have many specialists available."

    elif "appointment" in msg:
        return "You can book appointment online."

    elif "bye" in msg:
        return "Goodbye!"

    else:
        return "Sorry, I didn't understand."