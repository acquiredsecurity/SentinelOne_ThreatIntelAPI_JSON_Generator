from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Allow browser requests

# 🔹 Replace with your SentinelOne API details
SENTINELONE_API_URL = "https://<Console URL>/web/api/v2.1/threat-intelligence/iocs"
SENTINELONE_API_KEY = "<api key>"
# 🔹 Replace with your Webhook URL
WEBHOOK_URL = "https://<Console Url>/web/api/v2.1/hyper-automate/webhook/v1/webhook/http/<webhook key>"

@app.route('/submit', methods=['POST'])
def submit_json():
    try:
        data = request.json
        json_data = data.get("jsonData")
        submission_type = data.get("submissionType", "webhook")  # Default to webhook

        if not json_data:
            return jsonify({"error": "No JSON data received"}), 400

        headers = {"Content-Type": "application/json"}

        if submission_type == "sentinelone":
            # 🔹 Ensure API Key is set
            if not SENTINELONE_API_KEY:
                return jsonify({"error": "SentinelOne API Key is missing"}), 400

            # 🔹 Set API Authorization Header
            headers["Authorization"] = f"APIToken {SENTINELONE_API_KEY}"

            # 🔹 Send request to SentinelOne API
            response = requests.post(SENTINELONE_API_URL, headers=headers, json=json_data)

        else:
            # 🔹 Default: Send to Webhook
            response = requests.post(WEBHOOK_URL, headers=headers, json=json_data)

        return jsonify({
            "message": "Submission successful",
            "status_code": response.status_code,
            "response_text": response.text
        }), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
