import json
security_alert = {
    "alert_type": "Brute Force",
    "severity": "High",
    "count": 42
}
with open("report.json", "w") as file:
    json.dump(security_alert, file)
    print("Report saved successfully!")