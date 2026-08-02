from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "online",
        "bot": "Kick Moderation Bot"
    }

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(silent=True)

    print("\n========================")
    print("📨 New Event Received")
    print(data)
    print("========================\n")

    return jsonify({
        "success": True
    }), 200


if __name__ == "__main__":
    print("🚀 Server Started")
    app.run(host="0.0.0.0", port=8000, debug=True)