## Date: 2026-04-22

### What I tried
- I ran `ps aux` to see all the processes running on the system
- Then I ran `ps aux | grep nginx` to see processes with the name nginx
- I ran `htop` to get an interactive feed of the processes on the system. We can press q to quit.
- I ran `netstat -tulnp` to see all listening ports with process names where t= tcp, u= udp, l= listening, n=number and p= process
- Similar to netstat is using the command `ss -tulnp` whic is just a modern type
- The command `lsof -i` shows every open network connection on the system and the process that opened it
- To search for open network connection on a particular port like port 22 to know who's using it, we simply use `lsof -i :22`
- I ran `sudo apt install vim-runtime` to install vimtutor
- i used `grep 'Failed' ~/security-journey/fake-auth.log | awk '{print $11}'` to get ip addresses from text and `grep 'Failed' ~/security-journey/fake-auth.log | awk '{print $9}'` to get usernames. The `awk` is a text processing tool that reads text line by line and lets you manipulate it. It is a powerful tool for log analysis and used constantly by security engineers. `awk` splits the texts in the line by white spaces or simply splits the line into fields by whitespaces. Taking the example below
```
Jan  1  10:00:01  server  sshd[1234]:  Failed  password  for  root  from  10.0.0.1  port  22
 $1  $2    $3       $4       $5          $6        $7      $8   $9    $10     $11      $12  $13
 
So `$9` is the username and `$11` is the IP address. while `$0` is special as it prints the whole line

awk '{print $1}' # print first field 
awk '{print $1, $3}' # print first and third field 
awk '{print $NF}' # print last field (NF = number of fields)

awk is a full programming language
# Print lines where field 6 equals 'Failed' awk '$6 == "Failed" {print $11}' 
# Print lines longer than 50 characters awk 'length > 50' 
# Count occurrences awk '{count[$11]++} END {print count}'
```
- `grep 'Failed' ~/security-journey/fake-auth.log | awk '{print $11}' | sort | uniq`. In this command, `sort` aranges the IP address in ascending order while `uniq` ensures that each Ip address is unique that is, it appears exactly once.
- I created the command `grep -i 'failed' fake-auth.log | awk '{print $11}' | sort | uniq -c` which looks for failed authentication attempts in the log file, prints out the IP addresses only, sorts them and gives the count of duplicates. 
```
Reading the output like a security engineer:

- 10.0.0.1 attempted 2 failed logins — most suspicious, potentially brute forcing
- 10.0.0.2 and 10.0.0.3 attempted 1 each — could be opportunistic scanning

In a real environment with thousands of log lines, this single command instantly surfaces the most aggressive attackers by frequency. That's exactly what security operations centers do manually before automating it.
```
### What broke
-

### What I learned
- The `-r` in `rm -r` means recursive removal in that it goes into every subfolder and every subfolder inside that, all the way down deleting everything it find
- The `f` in `rm -rf` means force. This is one of the most dangerous commands in linux and in this context, it forcefully deletes files and folders without warning. Hence, we should always double check path before running it.
- The reason there is owner, group and everyone else permission is due to access control.
- Chmod 777 is dangerous as the CIA triad can be compromised.
- `/usr/bin/passwd` is the command that changes your password. Passwords are stored in `/etc/shadow` which requires root to modify.
- Privilege escalation is the process of starting as a regular user and abusing a SUID binary to gain root access. It is one of the first things attackers do after getting initial access to a system
- We use `grep` to find patterns inside files. 
```
grep 'error' logfile.txt ------This returns all lines containing error in the txt log file
grep -i 'error' logfile.txt ------This returns all lines containing error without case sensitivity
grep -n 'error' logfile.txt ------This includes the line numbers
grep -v 'error' logfile.txt ------This returns line that does not contain error
grep -r 'password' /etc/ ---- --This recursively finds all the lines containing password in the all the files in /etc/
grep -c 'failed' auth.log ------ This returns the count of occurences of failed in auth.log
```
- grep -r 'password' /etc/ is one of the the first commands an attacker would run as sometimes developers can leave plaintext passwords in configuration files. Also, using `-r` saves the attacker a lot of time instead of going thorugh the files and folders one by one
- We use find to locate files by properties
```
find / -name 'passwords.txt'--- find file with the exact file name
find /home -name '*.txt' --- find all .txt file under /home
find / -type f -name '*.log' --- finds all .log files only
find / -perm -4000 2>/dev/null --- finds all SUID files without error
find / -writable 2>/dev/null --- finds all files user can write to 
```
- `2>/dev/null` hides errors. `2` refers to error output, `>` redirects output to a file, and `/dev/null` is the blackhole of the linux system in that it destroys anything that is written to it. So the total commands means to take the error messages and throe them into the blackhole so they never appear. If not, there will be a lot of permission denied messages which could bury the real results.
- The `find / writable` command is one of the first thing an attacker runs after gaining initial access to the system. This is because any file that is writable and can be executed by a privileged process is a potential privilege escalation path.
```
An attacker looks for writable files because:
- A writable script that runs automatically = inject malicious code into it
- A writable cron job owned by root = make root execute your commands
- A writable SUID binary = replace it with malicious code that runs as root
It's not just privilege escalation — it's finding anywhere they can plant something that gets executed later, ideally by a more privileged process.
```
- Piping is the process of chaining commands in the sense that the output of a command becomes the input of the command after the pipe symbol `|`. This is useful to perform complex analysis without writing any code. Pipes basically connects commands.
```
ps aux | grep python # processes are listed; filters for python
cat auth.log | grep 'Failed' | wc -l # count Failed login attempts in the auth.log
ls -la | sort -k5 -n # list files sorted by size
```
- `wc -l` is used to count lines that survived the filter hence giving a number as final outpur. `wc` stands for word count while `-l` means count lines
- `sort -k5 -n` sorts files by size
- If we know a process Id say 1234, we can run the command `kill 1234` to politely ask the process to stop. Using `kill -9 1234` would force-kill the process immediately. However if there are multiple processes with the same name, we can run `killall firefox` to kill all preocesses with the name firefox.
- An attacker who lands on your system immediately runs netstat -tulnp to understand what services are running, what ports are listening, and what internal services are accessible
### Commands/code worth remembering
```code
gtfobins.github.io - documents every Linux binary that can be abused for privilege escalation

grep 'Failed' ~/security-journey/fake-auth.log | awk '{print $9, $11}'

grep 'Failed' ~/security-journey/fake-auth.log | awk '{print $11}' | sort | uniq
```

### Questions for later
- The command `sort -k5 -n` sorts size in ascending order but there are various types of sorting. What number should be put to use the various sorts?
- Is grep used for searching within files while find is for outside files and folders?
- What does this mean `[::]:52934  `
- What does this mean `[::1]:631  `
- What does this mean `[::]:* `
- What does this mean `0.0.0.0:*`
- What does this mean `224.0.0.251:5353  `
- What does this mean `127.0.0.53%lo:53 `
- What does this mean `:::52934  `
- What does this mean `::1:631  `
- What does this mean `:::*`

```
**1. `sort -k5 -n` and column numbers**

`-k` specifies which **column** to sort by. `-n` means sort numerically instead of alphabetically.

Run `ls -la` and count the columns:


-rw-r--r-- 1 alice staff 1234 Jan 1 myfile.txt
    1       2   3     4    5    6  7      8


So `-k5` sorts by column 5 which is file size.

Common useful sorts:

|Command|Sorts by|
|---|---|
|`sort -k5 -n`|File size (ascending)|
|`sort -k5 -rn`|File size (descending, `-r` reverses)|
|`sort -k3`|Username (column 3)|
|`sort -k6`|Month (column 6)|
|`sort -k9`|Filename (column 9)|
|`sort -u`|Remove duplicates while sorting|

---

**2. `grep` vs `find` — is grep inside files and find outside?**

Almost exactly right. The precise distinction:

- `grep` — searches **content inside files**. It reads file contents and finds matching lines.
- `find` — searches **the filesystem itself**. It finds files and directories based on their properties — name, size, permissions, owner, date modified. It doesn't read file contents.

The combination is powerful:

bash

```bash
# find the files, then grep inside them
find /etc -name '*.conf' | xargs grep 'password'


`xargs` takes the output of `find` and passes each filename as input to `grep`. This searches inside every `.conf` file in `/etc` for the word password.

That's a real attacker command.
```


```

**First, understand the two types of IP addresses:**

**IPv4** — the old format: `192.168.1.1` (four numbers separated by dots) **IPv6** — the new format: `2001:db8::1` (longer, uses colons, uses `::` as shorthand for zeros)

Most systems run both simultaneously. That's why you see both formats in `ss -tulnp`.

---

**Now your specific questions:**

**`0.0.0.0:*`** IPv4. `0.0.0.0` means "all network interfaces" — listening on every network card in your machine. The `*` means any port or any connecting address. So this service accepts connections from anywhere.

**`127.0.0.53%lo:53`** IPv4. `127.0.0.53` is a localhost address — only reachable from inside your own machine. `%lo` means it's specifically on the loopback interface. Port `53` is DNS. So this is your local DNS resolver — only your own machine can talk to it, nothing external.

**`224.0.0.251:5353`** IPv4. `224.x.x.x` is a **multicast** address — it broadcasts to multiple devices on your local network simultaneously. Port `5353` is mDNS (local network name resolution like `yourcomputer.local`). This is how devices find each other on a local network without a central DNS server.

**`[::]:52934`** and **`:::52934`** Both mean the same thing — just different ways of writing it. IPv6 equivalent of `0.0.0.0` — listening on all interfaces. The `[::]` notation is the full IPv6 any-address. `:::52934` is shorthand for the same thing. Port 52934 is a high random port — probably a temporary connection.

**`[::1]:631`** and **`::1:631`** Both mean the same thing. `::1` is the IPv6 equivalent of `127.0.0.1` — localhost only. So port 631 (printer service) is only reachable from your own machine. Nothing external can touch it.

**`[::]:*`** and **`:::*`** Both mean the same thing. IPv6, listening on all interfaces, accepting any connection. The `*` means no specific port or peer address restriction yet.


```
Quick Reference Table:

|Address|Type|Meaning|
|---|---|---|
|`0.0.0.0`|IPv4|All interfaces — reachable externally|
|`127.0.0.1`|IPv4|Localhost only — internal only|
|`127.0.0.53`|IPv4|Localhost DNS specifically|
|`224.x.x.x`|IPv4|Multicast — local network broadcast|
|`[::]` or `::`|IPv6|All interfaces — reachable externally|
|`[::1]` or `::1`|IPv6|Localhost only — internal only|
|`*`|Both|Any address or any port|

**Security Rule:**
- `0.0.0.0` or `[::]` = **externally reachable** — attackers can reach this from the internet
- `127.x.x.x` or `::1` = **internal only** — only reachable if already inside the system