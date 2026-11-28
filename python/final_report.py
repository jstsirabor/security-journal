import json

events = []
with open("final_auth.log", "r") as log:
    for line in log:
        line = line.strip()
        words = line.split()

        ip=""
        user =""

        for index, word in enumerate(words):
            if word == "from":
                ip = words[index + 1]
            if word == "for":
                user = words[index + 1]
        
        if "Failed" in line: 
            status = "Failed" 
        else: 
            status = "Accepted"

        event_dict = {"ip": ip, "user": user, "status": status}
        events.append(event_dict)
print(events)

attacker_counts = {}
for event in events:
    if event["status"] == "Failed":
        ip_address = event["ip"]
        attacker_counts[ip_address] = attacker_counts.get(ip_address, 0) + 1
print(attacker_counts)


report = {
    "total_events": len(events),
    "unique_attackers": len(attacker_counts),
    "attacker_details": attacker_counts
}

with open("fnal_report.json", "w") as file:
    json.dump(report, file, indent=4)
    print("Final JSON report generated successfully!")