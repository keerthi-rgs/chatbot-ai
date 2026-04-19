from chatbot import get_response

def test_hello():
    assert get_response("hello") == "Hi! How can I help you?"