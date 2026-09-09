### Section 1: Foundational Linux Directories

| Question | Answer |
|---|---|
| What does `/` represent in Linux? | The **root** of the entire filesystem. All other directories branch out from here. |
| What does `/etc` contain, and why do attackers target it? | System-wide configuration files. Attackers target it to steal credentials (like `/etc/shadow`) or change system behavior. |
| What does `/home` contain? | User personal folders (Documents, Desktop, Downloads) and user-specific configuration files (like `.bashrc`). |
| What does `/var/log` contain, and why is it important? | System and application logs. It's the "crime scene" — used to investigate what happened during a security incident. |
| What is special about `/tmp`, and why do attackers like it? | It is **world-writable** (anyone can write there). Attackers drop malicious scripts here because they have write access and it's often unmonitored. |
| What do `/bin` and `/usr/bin` contain? | Executable programs (commands) that users and the system run. |
| Why would an attacker tamper with `/bin/ls`? | They replace it with a malicious version that **hides their files** when you run `ls`, so you don't see their malicious activity. |

---

### Section 2: Navigation and File Management (Commands)

| Question | Answer |
|---|---|
| What does `pwd` do? | Prints the current working directory (tells you exactly where you are). |
| What is `cd /`? | Changes directory to the **root** of the filesystem. |
| What is `cd ~`? | Changes directory to your **home** folder (`/home/username`). |
| What does `cd ..` do? | Moves up one directory level (to the **parent** directory). |
| What does `cd .` do? | Stands for the **current** directory. Running `cd .` does nothing, but `./script.sh` runs a script from the current directory. |
| How do hidden files differ from normal files? | Hidden files start with a dot (`.`), e.g., `.bashrc`. They don't appear in a normal `ls`. |
| Why are hidden files a security concern? | They often contain configurations or startup scripts that run automatically (like `.bashrc`). Attackers can hide malicious code here. |

---

### Section 3: The Sticky Bit on `/tmp`

| Question | Answer |
|---|---|
| What permission string does `/tmp` usually have? | `drwxrwxrwt` |
| What does the `t` (sticky bit) do on `/tmp`? | It prevents normal users from deleting or renaming files they don't own in that directory. |
| Does the sticky bit stop `root` from deleting files? | No. `root` can delete any file, regardless of ownership. |

---

### Section 4: Command History & Evasion (Attacker Tradecraft)

| Question | Answer |
|---|---|
| Where is user command history stored? | `~/.bash_history` |
| What does `history -c` do? | Clears the **current terminal session's** in-memory history. |
| Does `history -c` clear the `~/.bash_history` file? | No. It only clears the current session's memory. The file on disk remains unchanged until overwritten. |
| What command forces the current terminal history to overwrite the `~/.bash_history` file? | `history -w` |
| Why would an attacker overwrite history with "normal" commands? | To make the history file look legitimate. A completely empty history is suspicious; a history full of boring commands (`ls`, `pwd`, `date`) is less likely to be investigated. |

---

### Section 5: Integrity Checking (Detecting Tampering)

| Question | Answer |
|---|---|
| How can you verify if a binary like `ls` has been tampered with? | Use `dpkg -V coreutils` or `dpkg -V | grep /bin/ls`. |
| What package does `ls` belong to on Ubuntu? | `coreutils` (Core Utilities). |
| In `dpkg -V` output, what does the `5` status code mean? | The checksum does not match the original package database — the file has been modified. |
| If `dpkg -V coreutils` returns no output, what does that mean? | All files in the package match the original checksums. The system is clean (for that package). |

---

### Section 6: Attack Chain Tradecraft

| Question | Answer |
|---|---|
| Why might an attacker not just clear all logs? | Empty logs or a completely blank `~/.bash_history` are a **red flag** to an investigator. |
| How does an attacker hide their command line history effectively? | They either **edit specific lines** in `~/.bash_history` (using `nano`), or **run normal commands** and then overwrite the file with `history -w`. |
| Where would an attacker drop a one-time malicious script, and why? | `/tmp` — because it is world-writable, and they don't need to worry about system integrity checks for a temporary file. |

