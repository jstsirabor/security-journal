alert = "ALERT: New failed login detected from IP 192.168.1.50\n"
with open("alerts.log", "a") as file:
    file.write(alert)
    print("Alert logged successfully.")