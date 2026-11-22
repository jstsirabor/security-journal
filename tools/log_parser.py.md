import json
failed_count = 0
with open("access.log", "r") as file:
    for line in file:
        line = line.strip()
        if "Failed" in line:
            failed_count += 1
report = {
    "target_file": "access.log",
    "failed_logins": failed_count
}
with open("analysis.json", "w") as file:
    json.dump(report, file)
    print("Analysis complete. Report saved.")
