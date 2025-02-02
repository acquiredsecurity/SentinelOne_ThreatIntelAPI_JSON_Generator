# SentinelOne_ThreatIntelAPI_JSON_Generator
The SentinelOne IOC JSON Generator is a web-based tool that allows users to manually input Indicators of Compromise (IOCs) and generate properly formatted JSON data for use with the SentinelOne API. It supports one or more entries, a structured optional fields section, and a built-in webhook submission feature for direct API integration.


Features
✅ Supports Various IOC Types (DNS, IPV4, IPV6, MD5, SHA1, SHA256, URL)
✅ Enter one or multiple IOCs at once
✅ Optional Fields Section (Easily expand/hide additional fields)
✅ Severity & Original Risk Score as Integers (Severity: 1-7, Risk Score: 0-100)
✅ Ensures Proper Capitalization (IOC Type remains uppercase for API compatibility)
✅ Download JSON or Copy to Clipboard (Save or copy generated JSON instantly)
✅ Submit to Webhook (Sends generated JSON directly to the configured SentinelOne API Webhook in HyperAutomation)

Dependencies and Setup
Installation & Setup (For Webhook Submission) Python Flask Server

1️ Install Python and required dependencies. Please fefer to the pythong guide to install Python 3 for your OS. Once Python is installed run the following command to ensure flask is installed. 
                pip install flask


2 Ensure the webhook endpoint is correctly configured in proxy_server.py.
                Update the URL in the file python proxy_server to match your webhook URL on line # 9 SENTINELONE_WEBHOOK_URL = "Enter your URL Here"

3 Run the Flask proxy server:
                python3 proxy_server.py


How to Use the Webform

1️⃣ Enter IOC details manually

Select an IOC Type (DNS, IPV4, MD5, etc.)
Choose Single Entry or Multiple Entries
Enter IOC values, source, and other relevant details

2️⃣ Optional Fields

Click Show/Hide Optional Fields to enter additional data (e.g., severity, threat actors, risk score).

3️⃣ Generate JSON

Click Generate JSON to format the input as a valid JSON object.

4️⃣ Download or Copy JSON

Click Download JSON to save the file.
Click Copy JSON to copy the generated output to the clipboard.

5️⃣ Submit to Webhook

Click Submit to Webhook to send the JSON directly to the SentinelOne API via a Flask proxy server. In order to receive the data to a webhook you will need to use the hyper automation feature and setup a webhook to  receive and send data to the API. Altertanely you can edit this to send dirctly to the API with your Site ID but you will need to adjust the code as necessary.


Technical Details
Built with HTML, CSS, JavaScript, and jQuery
Uses Flask (Python) as a proxy for API submissions
Ensures field validation & API-compliant formatting
Contributing & Support
If you encounter any issues or need enhancements, feel free to modify the source code or report a problem.

🚀 Enjoy using the SentinelOne IOC JSON Generator! 🚀

