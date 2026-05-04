**Log Analysis Pipeline** The foundation of security operations. Chain `grep`, `awk`, `sort`, `uniq` to extract signal from noise in log files. Real tools like fail2ban automate exactly this logic.

**Attacker Enumeration** After gaining access, attackers run:

- `grep -r 'password' /etc/` — find plaintext credentials in config files
- `find / -writable 2>/dev/null` — find files they can plant malicious code in
- `find / -perm -4000 2>/dev/null` — find SUID binaries for privilege escalation

**Living in the logs** Defenders live in `/var/log/`. Every attack leaves traces — failed logins, unusual processes, unexpected network connections. Reading logs fluently is as important as knowing attack techniques.

**`/dev/null`** A special file that destroys anything written to it. Used constantly to suppress unwanted output — especially error messages when searching system directories.