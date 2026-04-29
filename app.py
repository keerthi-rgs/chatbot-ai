from flask import Flask, request, jsonify, render_template
from chatbot import get_response   # import here
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "Invalid input"}), 400

        reply = get_response(data["message"])   # use function

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)