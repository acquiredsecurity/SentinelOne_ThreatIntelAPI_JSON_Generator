from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow browser requests

# SentinelOne Webhook URL
SENTINELONE_WEBHOOK_URL = "Enter your webhook URL Here" 

@app.route('/submit', methods=['POST'])
def submit_to_sentinelone():
    try:
        json_data = request.json  # Get JSON from frontend

        # Forward the request to SentinelOne
        response = requests.post(
            SENTINELONE_WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            json=json_data
        )

        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
