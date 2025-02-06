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

@app.route('/submit', methods=['POST', 'OPTIONS'])
def submit_json():
    if request.method == "OPTIONS":  # ✅ Handle preflight CORS request
        response = jsonify({"message": "CORS preflight successful"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        return response, 200

    try:
        data = request.json  # Get raw JSON sent from frontend

        # ✅ Log received JSON before processing
        print("\n===== RECEIVED JSON FROM WEBFORM =====")
        print(json.dumps(data, indent=4))

        json_data = data.get("jsonData", None)

        # ✅ Log extracted jsonData before processing
        print("\n===== EXTRACTED jsonData (Before Processing) =====")
        print(json.dumps(json_data, indent=4) if json_data else "No jsonData found")

        # ✅ Ensure jsonData exists
        if not json_data:
            return jsonify({"error": "No JSON data received"}), 400

        submission_type = data.get("submissionType", "webhook")
        headers = {"Content-Type": "application/json"}

        # ✅ Fix `siteIds` format: Ensure it's stored as a **list of strings**
        if "filter" in json_data and "siteIds" in json_data["filter"]:
            json_data["filter"]["siteIds"] = [str(site) for site in json_data["filter"]["siteIds"]]

        # ✅ Ensure correct data structure in `data`
        if isinstance(json_data.get("data"), list):
            for entry in json_data["data"]:
                if isinstance(entry, dict):  # ✅ Ensure each entry is a dictionary
                    if "type" in entry:
                        entry["type"] = entry["type"].upper()  # 🔹 Convert type to uppercase
                    if "source" in entry:
                        entry["source"] = str(entry["source"])  # 🔹 Convert source to string
                    if "originalRiskScore" in entry:
                        try:
                            entry["originalRiskScore"] = int(entry["originalRiskScore"])
                        except ValueError:
                            entry["originalRiskScore"] = 0  # 🔹 Default to 0 if invalid
                    if "severity" in entry:
                        try:
                            entry["severity"] = int(entry["severity"])
                        except ValueError:
                            entry["severity"] = 1  # 🔹 Default to 1 if invalid

        # ✅ Log final JSON before submission
        print("\n===== FINAL JSON SENT TO API/WEBHOOK =====")
        print(json.dumps(json_data, indent=4))

        # 🔹 **Fix the Double `data` Issue for Webhook Submissions**
        if submission_type == "webhook":
            if "data" in json_data:
                json_data = json_data["data"]  # ✅ Extract only the inner `data` contents

        if submission_type == "sentinelone":
            if not SENTINELONE_API_KEY:
                return jsonify({"error": "SentinelOne API Key is missing"}), 400

            headers["Authorization"] = f"APIToken {SENTINELONE_API_KEY}"

            # ✅ Log before sending to SentinelOne API
            print("\n===== SENDING TO SENTINELONE API =====")
            print(json.dumps(json_data, indent=4))

            response = requests.post(SENTINELONE_API_URL, headers=headers, json=json_data)

        else:
            # ✅ Log before sending to Webhook
            print("\n===== SENDING TO WEBHOOK (DATA HEADER FIXED) =====")
            print(json.dumps(json_data, indent=4))

            response = requests.post(WEBHOOK_URL, headers=headers, json=json_data)

        # ✅ Log API Response
        print("\n===== SENTINELONE RESPONSE =====")
        print(response.text)

        return jsonify({
            "message": "Submission successful",
            "status_code": response.status_code,
            "response_text": response.text
        }), response.status_code

    except Exception as e:
        print("\n🚨 ERROR: Exception Occurred!")
        print(str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
