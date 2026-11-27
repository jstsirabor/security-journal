import json

try:
    with open("scan_results2.json", "r") as results:
        json_results = json.load(results)
        for line in json_results:
            cve = line.get("cve", "No CVE found")
            target = line.get("target")
            print(f"Target: {target} vulnerability: {cve}")
except FileNotFoundError:
    print("File not found.")