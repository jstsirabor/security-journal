attacker_counts = {}

with open("server.log", "r") as log:
    for line in log:
        line = line.strip()
        if "Failed" not in line:
            continue

        line_content = line.split()

        for index, word in enumerate(line_content):
            if word == "from":
                ip_address = line_content[index + 1]
                if ip_address == "192.168.1.50":
                    continue

                attacker_counts[ip_address] = attacker_counts.get(ip_address, 0) + 1

print(attacker_counts)