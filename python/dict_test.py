security_alert = {
    "alert_type" : "Brute Force",
    "severity" : "High",
    "count" : 42    
}
print(security_alert)
print(security_alert["severity"])
print(security_alert.get("ip_address", "IP_NOT_FOUND"))

