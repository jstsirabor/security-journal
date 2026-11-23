import json
scan_results = [
    {"ip": "10.0.0.1", "open_ports": [80,443]},
    {"ip": "10.0.0.2", "open_ports": [22]}
]
print(scan_results)
print(scan_results[0]["ip"])
print(scan_results[1]["open_ports"])

for item in scan_results:
    print(f"IP: {item['ip']} and ports: {item['open_ports']}")

with open("scan_results.json", "w") as file:
    json.dump(scan_results,file, indent=4)