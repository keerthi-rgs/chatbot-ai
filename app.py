from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)