**What is a Process?** A process is any program currently running on the system. Every command you run, every service, every background task is a process with a unique PID (Process ID) and an owner.

**Viewing Processes**

| Command                | What it does                                               |
| ---------------------- | ---------------------------------------------------------- |
| `ps aux`               | Every running process with user, PID, CPU, memory, command |
| `ps aux \| grep nginx` | Find specific process by name                              |
| `htop`                 | Interactive process viewer (press q to quit)               |
| `kill 1234`            | Politely ask process 1234 to stop                          |
| `kill -9 1234`         | Force-kill process 1234 immediately                        |
| `killall firefox`      | Kill all processes named firefox                           |

**Security use of `ps aux`:**

bash

```bash
# Find credentials passed as command line arguments
ps aux | grep -i 'password\|secret\|token\|key'
```

Developers sometimes pass credentials as arguments — these appear in plain text in process listings.

**Network Connections**

|Command|What it does|
|---|---|
|`ss -tulnp`|All listening ports with protocol and process|
|`lsof -i`|Every open connection with process name and user|
|`lsof -i :22`|Zoom into specific port|
|`netstat -tulnp`|Older alternative to ss (same flags)|

**ss -tulnp Column Reference**

|Column|Meaning|
|---|---|
|Netid|Protocol: tcp or udp|
|State|LISTEN = waiting, UNCONN = UDP open|
|Recv-Q|Data received not yet processed|
|Send-Q|Data queued to send|
|Local Address:Port|What IP/port your machine listens on|
|Peer Address:Port|Who is connected (* = nobody yet)|
|Process|Program that owns the port|

**Common Ports to Know**

|Port|Service|
|---|---|
|22|SSH — remote access|
|53|DNS — domain name resolution|
|80|HTTP — web traffic|
|443|HTTPS — encrypted web|
|631|CUPS — printer service|
|3306|MySQL database|
|5432|PostgreSQL database|

**ss vs lsof — Key Difference**

- `ss -tulnp` — shows what ports are **waiting** for connections
- `lsof -i` — shows what is **actively connected** right now