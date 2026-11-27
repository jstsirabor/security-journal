## Date: 2026-11-26

### What I tried
- grep "Failed" auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr | head -n 3
- In Wireshark, what filter would you type to see only these SYN packets? tcp.flags.syn  == 1
```python
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
```
---
```bash
#!/bin/bash

filename="$1"

if [ -z "$filename" ]; then
    echo "Error: No file provided"
    exit 1
elif [ ! -f "$filename" ]; then
    echo "Error: File does not exist"
    exit 1
else
    echo "File found. Counting lines..."
    wc -l < "$filename"
fi
```
---
```
import json

with open("scan.txt", "r") as report:
    lines = report.readlines()
    open_ports = [port.strip() for port in lines if "open" in port]

with open("filtered_scan.txt", "w") as filtered_report:
    for port in open_ports:
        filtered_report.write(port + "\n")
    print("Filtered scan saved.")
```
### What broke
- 

### What I learned
- A SYN flood. The server allocates a tiny bit of memory for every half-open connection in the "SYN queue." If you send 10,000 spoofed SYNs, the queue fills up and legitimate users can't connect (Denial of Service).
- _This specific error, `Expecting value: line 1 column 1 (char 0)`, is the #1 most common JSON error in the world. It almost always means "The file is empty._
- Bash does **not** use parentheses `()` for `if` statements. It uses square brackets `[ ]`. And spaces are mandatory.
- In bash, `else` does not take a semicolon. Just `else` on its own line.
- if statement in bash ends with fi
- is file empty -z, is it a regular file -f
- ### Drill 1 Notes: The Log Pipeline
	- **The Goal:** Extract Top 3 IPs from a log.  
	- **Your Mistake:** You used `awk {print $10}` and missed the final sorting.  
	- **The Top 1% Rules:**  
	    1. **Quote your awk:** `awk '{print $10}'`. Without quotes, Bash tries to interpret the `{}`.
	    2. **The Field Shift Trap:** You cannot rely on `$10` if the log says "invalid user test from...". The IP shifts. You must use the loop: `for(i=1;i<=NF;i++) if($i=="from") print $(i+1)`.
	    3. **Top 3 Pipeline:** `... | sort | uniq -c | sort -nr | head -n 3`. (Sort for `uniq`, then sort numerically reverse for the highest counts).
- ###  Drill 2 Notes: Networking & Wireshark
	- **The Goal:** Explain why IP spoofing fails on TCP and write a Wireshark filter.  
	- **Your Mistake:** Typo in the Wireshark filter (`tcp.--.syn`).  
	- **The Top 1% Rules:**  
	    1. **Wireshark Syntax:** It is `tcp.flags.syn == 1`. No dashes.
	    2. **The TCP Spoof Flaw:** IP spoofing fails for TCP because the server sends the `SYN-ACK` to the spoofed IP. The attacker never gets it, so the handshake dies.
	    3. **The DoS Use Case:** Because it fails for TCP, spoofing is used for "blind" attacks like SYN Floods (filling the server's SYN queue with half-open connections).
- ### Drill 3 Notes: Python JSON Parser

	- **The Goal:** Load JSON data, handle missing keys.
	- **Your Mistake:** Trying to use `.get()` on a raw string (before `json.load()`).    
	- **The Top 1% Rules:**
	    1. **Unpacking:** You must use `json.load(file)` to convert the raw text into a Python list/dictionary. You cannot call dictionary methods (`.get()`) on the raw text.
	    2. **The Empty File Trap:** The error `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` almost always means the file you are trying to parse is empty.
	    3. **The Safe Get:** Always use `.get("key", "Default")` so your script doesn't crash with a `KeyError` if the field is missing.
- ### Drill 4 Notes: Bash Conditionals
	- **The Goal:** Check if a file argument exists.  
	- **Your Mistake:** Used `else if` instead of `elif`, and duplicated the `-z` check.  
	- **The Top 1% Rules:**  
	    1. **Bash `elif`:** Bash uses `elif`, NOT `else if`.
	    2. **Spaces Matter:** `if [ -z "$var" ]` requires spaces inside the brackets. `if [-z "$var"]` will crash.
	    3. **The `-f` Check:** `-z` checks if a string is empty. `-f` checks if the file exists. You need two separate checks.
- ### Drill 5 Notes: Python File I/O & List Comprehensions
	- **The Goal:** Read a file, filter lines, write to a new file.  
	- **Your Mistake:** `.write(var1, var2)` syntax error, and not using `.strip()` in the list comprehension.
	- **The Top 1% Rules:**  
	    1. **`.write()` Syntax:** It only takes **one** argument. `file.write(text)`. If you want a newline, you must add it manually: `file.write(text + "\n")`.
	    2. **List Comprehension Stripping:** If you want the cleaned data in your new list, you must strip it _inside_ the comprehension: `[line.strip() for line in lines if "open" in line]`.
	    3. **Indentation:** `print()` outside the `for` loop runs once. Inside the loop, it runs on every iteration.


### Commands/code worth remembering
```code

```

### Questions for later
-