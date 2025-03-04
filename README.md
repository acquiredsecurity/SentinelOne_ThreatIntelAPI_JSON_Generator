# SentinelOne_ThreatIntelAPI_JSON_Generator
The SentinelOne IOC JSON Generator is a web-based tool that allows users to manually input Indicators of Compromise (IOCs) and generate properly formatted JSON data for use with the SentinelOne API. It supports one or more entries, a structured optional fields section, and a built-in webhook submission feature to submit via a Webhook with Hyper Automation or directly to the SentienlOne API.

<img width="583" alt="image" src="https://github.com/user-attachments/assets/8ecd6e40-45ba-4d5a-b5f2-718cb8fd059e" />



Features
✅ Supports Various IOC Types (DNS, IPV4, IPV6, MD5, SHA1, SHA256, URL)  
✅ Enter one or multiple IOCs at once  
✅ Optional Fields Section (Easily expand/hide additional fields)  
✅ Severity & Original Risk Score as Integers (Severity: 1-7, Risk Score: 0-100)  
✅ Ensures Proper Capitalization (IOC Type remains uppercase for API compatibility)  
✅ Download JSON or Copy to Clipboard (Save or copy generated JSON instantly)  
✅ Submit to Webhook (Sends generated JSON directly to the configured SentinelOne API Webhook in HyperAutomation)  
✅ Submit directly to API (Sends generated JSON directly to the configured SentinelOne API)  

**Dependencies and Setup**  
Installation & Setup (For Webhook Submission) Python Flask Server  

1️ Install Python and required dependencies. Please refer to the python guide to install Python 3 for your OS. Once Python is installed run the following command to ensure flask is installed.   
                pip install flask  


2 Ensure the webhook endpoint is correctly configured in proxy_server.py.  
                Update the following Variables in the file:  
                          SENTINELONE_API_URL = "https://<your URL>/web/api/v2.1/threat-intelligence/iocs"  
                          SENTINELONE_API_KEY = "<API Key>"  
                          WEBHOOK_URL = "<Webhook URL>"  

3 Run the Flask proxy server:  
                python3 proxy_server.py  



***************************  
💡 How to Use the Webform  
1️⃣ Enter IOC Details Manually  
Select an IOC Type (DNS, IPV4, MD5, etc.)  
Enter IOC values, source, and other relevant details  
Choose multiple entries (one per line)  

2️⃣ Optional Fields  
Click "Show/Hide Optional Fields" to enter additional data  
(e.g., severity, threat actors, risk score, category, etc.)  

3️⃣ API Filtering (Optional)  
Click "API Submission" to enable direct API filtering. The filter fields are handled in the webhook so they are not needed for webhook submissions. Enter Site IDs, Account IDs, Group IDs, or Tenant scope for targeted submissions. 

4️⃣ Generate JSON  
Click "Generate JSON" to format input into a valid JSON object.  
JSON is automatically formatted for SentinelOne API compliance.  

5️⃣ Download or Copy JSON  
Click "Download JSON" to save the file.  
Click "Copy JSON" to copy the JSON output to the clipboard.  

6️⃣ Submit JSON  
"Submit to Webhook" → Sends JSON via the SentinelOne HyperAutomation Webhook API.  
"Submit to API" → Sends JSON directly to SentinelOne Threat Intelligence API.  
  
******************  




Technical Details
Built with HTML, CSS, JavaScript, and jQuery  
Uses Flask (Python) as a proxy for API submissions  
Ensures field validation & API-compliant formatting  
Contributing & Support  
If you encounter any issues or need enhancements, feel free to modify the source code or report a problem.  

🚀 Enjoy using the SentinelOne IOC JSON Generator! 🚀  

