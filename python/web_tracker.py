"""
Create the log file in your terminal first:

bash
cat > web_access.log << 'EOF'
203.0.113.5 - - [10/Oct/2026] "GET /login.php" 404 - "Mozilla"
203.0.113.5 - - [10/Oct/2026] "GET /admin.php" 404 - "Mozilla"
10.0.0.15 - - [10/Oct/2026] "GET /home" 200 - "Mozilla"
203.0.113.5 - - [10/Oct/2026] "GET /wp-config.php" 404 - "Mozilla"
198.51.100.10 - - [10/Oct/2026] "GET /secret.txt" 404 - "Googlebot"
198.51.100.10 - - [10/Oct/2026] "GET /robots.txt" 200 - "Googlebot"
203.0.113.5 - - [10/Oct/2026] "GET /backup.sql" 404 - "Mozilla"
192.168.1.100 - - [10/Oct/2026] "GET /profile" 404 - "Mozilla"
EOF
Your Mission:
Write a Python script called web_tracker.py.

Create an empty dictionary attacker_counts = {} to track IPs.

Create an empty list suspicious_paths = [] to track the files they are looking for.

Open web_access.log and loop through it line by line.

Strip the newlines.

The Logic Filter: Only look at lines that represent a "File Not Found" error. You can do this by checking if " 404 " is in the line. If it is not, use continue to skip the line. (Note: the spaces around 404 are important to avoid matching a URL that has 404 in its name).

The Extraction:

Use .split() to chop the line.

The IP address is always the very first word (index 0).

To find the path they requested (e.g., /login.php), use enumerate() to look for the word "GET". The path is the word immediately after "GET".

The path will have quotes around it (e.g., "/login.php"). Use .strip('"') to remove the quotes.

The Allowlist: If the IP address is "198.51.100.10" (Googlebot) OR "192.168.1.100" (Internal IP), skip it using continue.

The Tally:

Add the cleaned path to your suspicious_paths list using .append().

Add the IP to your dictionary using the counter idiom: attacker_counts[ip_address] = attacker_counts.get(ip_address, 0) + 1.

Print both the attacker_counts dictionary and the suspicious_paths list.
"""


attacker_counts = {}
suspicious_paths = []

with open("web_access.log", "r") as content:
    for line in content:
        line = line.strip()
        if " 404 " not in line:
            continue
        line = line.split()
        ip_address = line[0]
        
        path = ""
        for index, word in enumerate(line):
            if word.strip('"') == "GET":
                path = line[index + 1].strip('"')
        if ip_address == "198.51.100.10" or ip_address == "192.168.1.100":
           continue
            
        suspicious_paths.append(path)
        attacker_counts[ip_address] = attacker_counts.get(ip_address, 0) + 1

print(attacker_counts)
print(suspicious_paths)