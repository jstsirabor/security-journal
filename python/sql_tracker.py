import json
# The Extraction

sql_events = []

with open("sql_errors.log", "r") as log:
    for line in log:
        line = line.strip()
        words = line.split('"')
        
        ip_address = line.split()[3]
        status = words[2].strip()
        payload = words[1]
        track_dict = {"ip" : ip_address, "payload": payload, "status": status}
        sql_events.append(track_dict)
        print(sql_events)

# The Analysis
attacker_counts = {}

for event in sql_events:
    if event["status"] == "500":
        ip = event["ip"]
        attacker_counts[ip] = attacker_counts.get(ip, 0) + 1

# The Export

report = {
    "total_events" : len(sql_events),
    "unique_attackers" : len(attacker_counts),
    "attackers" : attacker_counts
}

with open("sql_report.json", "w") as file:
    json.dump(report, file, indent=4)
    print("SQL Report generated!")