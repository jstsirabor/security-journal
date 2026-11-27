import json

with open("scan.txt", "r") as report:
    lines = report.readlines()
    open_ports = [port.strip() for port in lines if "open" in port]

with open("filtered_scan.txt", "w") as filtered_report:
    for port in open_ports:
        filtered_report.write(port + "\n")
    print("Filtered scan saved.")