**Navigation Commands**

- `pwd` — shows your current location in the filesystem
- `ls` — lists files and folders in current location
- `ls -l` — detailed list with permissions, owner, size, date
- `ls -la` — same but includes hidden files (dot files)
- `cd Documents` — move into Documents folder
- `cd ..` — move up to parent directory
- `cd ~` — jump to your personal home directory
- `cd /` — jump to root of entire filesystem

**Key Concepts**

- Dot files (`.bashrc`, `.profile`) are hidden by default — not for security, but to keep file views clean and protect personal configuration from accidental deletion
- `.bashrc` runs automatically every time you open a terminal — contains aliases, environment variables, custom prompt settings
- Hidden = configuration, not necessarily sensitive

**Directory Map**

| Directory  | Purpose                         | Security Relevance                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/`        | Root — top of entire filesystem | Everything lives here                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `/etc`     | System configuration files      | Passwords, network settings, service configs                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `/home`    | Personal user directories       | Your files, scripts, dot files. First stop for stealing credentials and secrets (keys, passwords and bash history) to move deeper into the system.                                                                                                                                                                                                                                                                                                              |
| `/var/log` | Log files                       | Authentication events, attack evidence. `/var/log` is where attacks leave footprints. A brute-force attack shows up as thousands of failed SSH attempts. If logs are suddenly missing, that's itself a signal — an attacker wiped their tracks. Without reading logs, you can't investigate incidents or prove compliance to auditors.                                                                                                                          |
| `/tmp`     | Temporary files                 | Writable by everyone — attackers drop tools here. /tmp can be used to drop attacking tools that might not be discovered as its a directory that is used regularly and is writable/acessable by everyone                                                                                                                                                                                                                                                         |
| `/usr/bin` | Everyday user tools             | Python, curl, wget — attacker living-off-the-land. If an attacker replaces a real command here with a fake one (a "trojaned binary"), every time you run `ls` or `ssh`, you're actually running their code. Also, this is where you find **SUID binaries** — programs that run with root privileges even when a normal user launches them. Those are goldmines for privilege escalation.                                                                        |
| `/bin`     | Essential survival programs     | Bare minimum to boot and repair the system. If an attacker modifies something in `/bin`, the system might not even boot properly — or worse, it boots but every basic command is compromised from the ground up. Also, `/bin` vs `/usr/bin` separation matters: in a compromised system, `/bin` might be the only trusted partition left. Security people check hashes/signatures here because if `bash` itself is trojaned, you can't trust anything you type. |

**Living off the land** — attackers use tools already on the system (`python3`, `curl`, `nc`) rather than bringing their own, because existing tools are less detectable.

![[Pasted image 20260719181339.png]]

![[Pasted image 20260719172038.png]]
### `/` — Root directory
- The top of the entire filesystem tree
- **Security relevance:** If an attacker gains root access, they own everything under `/`. Compromising `/` means compromising the entire machine.

### `/etc` — System configuration
- Holds system-wide config files: `/etc/passwd`, `/etc/shadow`, `/etc/ssh/sshd_config`, `/etc/crontab`
- **Security relevance:** Misconfigurations live here. Weak SSH settings, bad permissions on `/etc/shadow`, malicious cron jobs — this is where defenders harden and attackers probe.

### `/home` — User directories
- Every user's personal folder: downloads, documents, browser data, SSH keys, bash history
- **Security relevance:** Attackers loot `/home` first after compromising an account. SSH keys, saved credentials, and bash history are all here.

### `/var/log` — System logs
- Event records: login attempts, service crashes, sudo commands, firewall blocks
- **Security relevance:** Attacks leave footprints here. Brute force shows as thousands of failed SSH attempts. Missing logs can mean an attacker wiped their tracks. Without logs, you can't investigate or prove compliance.

### `/tmp` — Temporary files
- Writable by everyone. Files usually deleted on reboot but live until then
- **Security relevance:** Attackers drop malware and payloads here because it's accessible, unmonitored, and blends in with normal system use.

### `/usr/bin` — User binaries
- Everyday commands: `ls`, `cd`, `grep`, `python3`, `ssh`
- **Security relevance:** Trojaned binaries here mean every command you run could be attacker code. Also contains SUID binaries — programs that run with root privileges, prime targets for privilege escalation. Attackers can drop trojaned binaries in `/usr/bin`, and the SUID programs here can be abused for privilege escalation.

### `/bin` — Essential system binaries
- Critical commands needed to boot and recover: `bash`, `cp`, `mv`, `rm`
- **Security relevance:** If `/bin` is compromised, you can't trust anything on the system. These are checked with hashes/signatures because a trojaned `bash` poisons every command you type.


## Key insight
- "I should always think like a security person" — not just "what is this?" but "how do I break it, how do I defend it, what does an attacker see?"

## Checkpoints (done from memory)
- [x] `/` is the root — compromise it, compromise everything
- [x] `/etc` holds configs — misconfigurations = vulnerabilities
- [x] `/home` is where attackers loot for credentials
- [x] `/var/log` shows attack footprints and missing logs = wiped tracks
- [x] `/tmp` is a malware drop zone because everyone can write there
- [x] `/usr/bin` has SUID binaries and trojan potential
- [x] `/bin` is critical to boot — if it's bad, trust nothing