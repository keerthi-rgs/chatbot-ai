from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "hi" in msg or "hello" in msg:
        reply = "Hello! How can I help you?"

    elif "name" in msg:
        reply = "I am your chatbot 🤖"

    elif "how are you" in msg:
        reply = "I'm doing great! 😊"

    elif "doctor" in msg:
        reply = "We have cardiologists, neurologists, and general physicians."

    elif "appointment" in msg:
        reply = "You can book appointment from our hospital portal."

    elif "time" in msg:
        reply = "Our hospital is open from 9 AM to 8 PM."

    elif "bye" in msg:
        reply = "Goodbye! Take care 👋"

    else:
        reply = "Sorry, I didn't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)