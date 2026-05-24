| Command                         | Action                                         |
| ------------------------------- | ---------------------------------------------- |
| `whoami`                        | Show current username                          |
| `sudo whoami`                   | Run a command as root (requires password)      |
| `sudo -l`                       | List commands you are allowed to run with sudo |
| `id`                            | Display UID, GID, and all group memberships    |
| `cat /etc/passwd`               | List all user accounts on the system           |
| `cat /etc/shadow`               | View password hashes (requires root)           |
| `ls -l /etc/passwd /etc/shadow` | Check permissions on these critical files      |

### /etc/passwd Field Structure

|Field|Example|Meaning|
|---|---|---|
|1|root|Username|
|2|x|Password placeholder (hash in /etc/shadow)|
|3|0|User ID (UID)|
|4|0|Group ID (GID)|
|5|root|Comment / Full name|
|6|/root|Home directory|
|7|/bin/bash|Default shell|

### Privilege Escalation Audit for NOPASSWD Entries

|Check|Question|
|---|---|
|#1 Writable|Can your user modify the script or binary?|
|#2 PATH Hijack|Does the script call external commands without full paths?|
|#3 Library Injection|Does the script import libraries that could be injected via environment variables (PYTHONPATH, PERL5LIB, etc.)?|

### Key Groups to Audit

|Group|Why It Matters|
|---|---|
|**sudo**|Can run commands as root — check `sudo -l` immediately|
|**adm**|Can read system logs without root — intelligence goldmine|
|**docker**|Can escape containers to host via socket abuse|
|**vboxusers**|Potential VM escape or host file access|
|**dip**|Network tool access — possible traffic interception|
