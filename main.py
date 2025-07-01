from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook is live!", 200

@app.route("/tweet", methods=["POST"])
def tweet():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify({"status": f"Received: {text}"}), 200
