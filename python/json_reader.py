import json
with open("scan_results.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data[1]["ip"])