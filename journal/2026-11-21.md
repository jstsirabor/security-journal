## Date: 2026-11-21

### What I tried
```
def check_login(username, failed_attempts):
    if failed_attempts >= 5:
        return f"ALERT: {username} has {failed_attempts} failed attempts"
    else:
        return f"OK: {username} is within normal limits"

admin = check_login("admin", 6)
print(admin)
guest = check_login("guest", 2)
print(guest)
--------------------------
ALERT: admin has 6 failed attempts
OK: guest is within normal limits
```
---
```
user_input = "22"
try:
    int_convert = int(user_input)
    print(f"Successfully converted {user_input} to an integer: {int_convert}")
except ValueError:
    print(f"Error: {user_input} is not a valid number!")
----
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/error_handler.py
Error: twenty-two is not a valid number!
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/error_handler.py
Successfully converted 22 to an integer: 22
```
---
```
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print characters from index 0 to 5 (not including 5)
print(text[0:5])
# Print characters from index 10 to the end
print(text[10:])
# Print the last 5 characters
print(text[-5:])
```
---
```
filename = "/etc/fake_file.txt"
try:
	with open(filename, "r") as file:
		content = file.read()
		print(f"{filename} file opened successfully")
		print(content)
except FileNotFoundError:
	print(f"Error: The {filename} file does not exist")
except PermissionError:
	print(f"Error: You do not have the permission to read the {filename} file.")
------------------------------------
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/safe_reader.py
Error: You do not have the permission to read the /etc/sudoers file.
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/safe_reader.py
Error: The /etc/fake_file.txt file does not exist
```
---
```
def scan_target(ip_address, port=80):
    return f"Scanning {ip_address} on port {port}..."

scan_result = scan_target("192.168.1.1", 22)
print(scan_result)
----------------------------------
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/default_args.py
Scanning 192.168.1.1 on port 80...
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/default_args.py
Scanning 192.168.1.1 on port 22...
```
---
```
with open("access.log", "r") as file:
	for line in file:
		print(line.strip())
```
---
```
security_alert = {
	"alert_type" : "Brute Force",
	"severity" : "High",
	"count" : 42
}

print(security_alert)
print(security_alert["severity"])
print(security_alert.get("ip_address", "IP_NOT_FOUND"))
```
---
```
import json
security_alert = {
	"alert_type" : "Brute Force",
	"severity" : "High",
	"count" : 42
}
report = json.dumps(security_alert)
print(report)
----------------------------------------
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/json_test.py
{"alert_type": "Brute Force", "severity": "High", "count": 42}
```
---
```
import json
security_alert = {
	"alert_type": "Brute Force",
    "severity": "High",
    "count": 42
}
with open("report.json", "w") as file:
	json.dump(security_alert, file)
	print("Report saved successfully!")
---------------------------------------------
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/json_file.py
Report saved successfully!
darkhand@darkhand:~/Documents/Tech/My-code/python$ cat report.json
{"alert_type": "Brute Force", "severity": "High", "count": 42} 
```
---
```
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
-------------------------------------------------
darkhand@darkhand:~/Documents/Tech/My-code/python$ /usr/bin/python3 /home/darkhand/Documents/Tech/My-code/python/log_parser..py
Analysis complete. Report saved.
darkhand@darkhand:~/Documents/Tech/My-code/python$ cat analysis.json
{"target_file": "access.log", "failed_logins": 1}darkhand@darkhand:~/Documents/Tech/My-code/python$ 
```
### What broke
-

### What I learned
- Function collects raw materials which are  the paremeter, ti then does a specific job and spits out the finished product using the `return` keyword
- If you just `print()` inside a function, it’s like a machine that puffs smoke into the air for anyone to see. If you `return` a value, it’s like the machine handing you the finished product so you can store it in a box and use it later.
```
def function_name(parameter1, parameter2):
    # do something
    return result
```
- We use the try/except to catch errors which could make the whole script crash. For instance, if we're scanning 1,000 ports, we don't want the scanner to crash because a certain port timed out. We can catch the timeout, log it and move on to the next port
```
try:
    # code that might fail
except ErrorType:
    # what to do if it fails
```
- However, `try/except` does not magically know how to skip lines in a loop. If you wrap the _entire_ file reading process in a `try` block and it hits an error on line 500, the whole `try` block aborts. To actually skip line 500 and keep going, the `try/except` **must be inside the loop**, and you must explicitly `continue`.
```
for line in log_file:
    try:
        # Try to process the line (e.g., convert a port to an int)
        port = int(line)
    except ValueError:
        # It failed! Log it and explicitly skip to the next line.
        print(f"Skipping malformed line: {line}")
        continue  # <--- THIS is what skips to the next line
```
- For except, there's the `ValueError` which is a data type error. There's also the `FileNotFoundError` which occurs when the file to be used is not found. Then there's also the `PermissionError` when we don't have the permission to access the file
- To read a file, use the `with open(filename, r) as file`. Also, to open the same file, use the `file.read()` and save the content i a variable which can then be printed
- `with open(...) as file:`. This is a "Context Manager." It guarantees that the file is closed automatically, even if your code crashes while reading it. If you don't use `with`, a crash might leave the file locked in memory. If the file doesn't exist (`FileNotFoundError`) or you don't have permission (`PermissionError`), the `open()` function fails _before_ the file is ever opened. You can't close a file that was never opened. The `with` statement handles closing for files that _do_ open, even if the reading process crashes.
- There's default argument in Python such that if no argument is given by the user, the default is used automatically else it is overridden. This is useful when writing a function to scan a port. Most scans might default to port `80` (HTTP), but you want to be able to pass in `443` when needed.
```
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Justus")                 # Uses default: "Hello, Justus"
greet("Justus", "Good morning") # Overrides: "Good morning, Justus"
```
- For large files like a massive serve log, we don't use .read() to read the file because it would dump the entire log into the computer memory all at once. So we have to use a for loop to read it one line at a time.
```
with open("test.log", "r") as file:
    for line in file:
        print(line)
```
- If you _really_ want to use the home directory shortcut in Python, you must use the `os` module:
```
import os
path = os.path.expanduser("~/Desktop/access.log")
```
- Every line in a text file ends with a hidden "newline" character (`\n`).  
When your Python `for` loop reads the line, it includes that hidden `\n`. Then, when you use `print()`, Python adds _its own_ newline at the end. So you get two newlines: one from the file, one from print. This is a massive problem for log parsing. If you try to search for the word `"admin"`, Python won't find it because the string is actually `"admin\n"`. 
	To fix this, we use the `.strip()` method on the line. `.strip()` removes all invisible whitespace (spaces, tabs, newlines) from the beginning and end of a string.
- A dictionary is like a real-life phone book in that we look for a person's name which is the key to get a value which would be their phone number
- A dictionary is enclosed in curly braces {} and uses colon : to separate keys and values
```
user = {
    "username": "admin",
    "ip_address": "192.168.1.5",
    "failed_attempts": 6
}
```
- If we try to access a key in a  dictionary  that doesn't exist, Python will throw a KeyError and the script will crash. To avoid this, we use the `.get()` method which asks for a key and if the key doesn't exist, it returns None or any default value we specify
	security_alert.get("ip_address", "IP_NOT_FOUND")
- In a real log file, you might have 10,000 lines. 9,999 of them have an IP address, but one line got corrupted and is missing the IP. If you don't use `.get()`, your script crashes on line 10,000. With `.get()`, it logs `IP_NOT_FOUND`, and keeps moving.
- JSON is a standard text format for storing data. It looks like a Python dictionary but it's a string
- When we write a tool that scans a network, we don;t just want it to print text to the screen. What we want to do is to savethe results to a file liek report.json so that another tool or a dashboard can read it later
- JSON is the universal language for API and security reports
- Python has a built-in library called json
	- `json.dumps(dictionary)` converts a Python dictionary into a JSON string
	- `json.loads(json_string)` converts a JSON string back to a python dictionary
- In Python, dictionaries use single quotes (`'alert_type'`). But in **JSON**, the standard strictly requires double quotes (`"alert_type"`).
- In real life, you rarely just `print` your JSON to the screen. You save it to a file so it can be used later. This is exactly how professional security tools (like Nmap, Burp Suite, or custom scanners) export their data.
	**The Difference:**
	- `json.dumps()` (with an **s**) returns a **s**tring.
	- `json.dump()` (without an **s**) writes directly to a **file**.
```
with open("report.json", "w") as file:
    json.dump(security_alert, file)
```
- Large files can be read fully, but line-by-line processing is usually more memory-efficient and scalable.
- `.strip()` removes all leading/trailing whitespace—not only `\n`. For log evidence where spacing matters, prefer `line.rstrip("\n")`.
	- In forensics, **you never destroy evidence**. If an attacker intentionally puts spaces at the beginning or end of a log line to trick a parser, `.strip()` would delete them, destroying the evidence. `.rstrip("\n")` only removes the newline character at the _right_ (end) of the string, preserving the actual data.
- `~` is not expanded automatically by `open()`, but Python can expand it safely with `Path("~/Desktop/access.log").expanduser()`.
```
from pathlib import Path
file_path = Path("~/Desktop/access.log").expanduser()
```
- `.get("ip_address", "IP_NOT_FOUND")` avoids `KeyError`, but a sentinel should not be mistaken for a real IP. Track missing fields separately where they matter.
- A Python dictionary maps to a JSON object; JSON is text with its own types (`true`, `false`, `null`), not literally a Python dictionary.
- `if "Failed" in line` counts matching text lines. For a real parser, describe it as “lines containing `Failed`,” unless you validate the log format and event fields.
	- Imagine an Apache web server log that says: `GET /login?error=Failed HTTP/1.1`. Your script would count that as a failed login. But it might not be an SSH failed login! To claim you found a "failed login," you must verify the format (e.g., ensuring the line actually contains `sshd` and `password`).
- Slicing lets you grab a specific chunk of a string using square brackets and colons: `[start:stop]`.
	- `[0:3]` means "start at index 0 and stop _before_ index 3."
    - `[-5:]` means "start 5 characters from the end and go to the end."    
	**Why a security engineer cares:** If you have a hash string like `"5f4dcc3b5aa765d61d8327deb882cf99"`, you might need to slice off the first 8 characters to compare it to a signature in a database.
- Opening a file with mode "w" empties it immediately so never use it on evidence
- **`//`** doesn't "drop the remainder". It floors toward negative infinity, so `-7 // 2` is `-4`, not `-3`.
- **`.strip()`** only removes whitespace at the start and end of the string, not "all spaces". It doesn't touch spaces in the middle.
### Commands/code worth remembering
```code

```


### Questions for later
-