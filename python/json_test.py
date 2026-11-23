import json

security_alert = {
	"alert_type" : "Brute Force",
	"severity" : "High",
	"count" : 42
}

report = json.dumps(security_alert)
print(report)