The target website is scanme.nmap.org with IPv4 address of 45.33.32.156. I found the operating system as Linux using nmap -sV command . Its rDNS is ack.nmap.org

During the scan, I found three open ports which are Port 22, 80 and 9929.
- Port 22 is SSH which  was running on OpenSSH 6.6.1p1 which is an old version that may have be potentially vulnerable to historical to CVEs
- Port 80 is HTTP which is running a webserver ad the NMAP scripts revealed the page title saying "Go ahead and Scanme"
- Port 9929 is nping-echo which is Nmap's echo server

Then I also came across filtered ports which are ports whose traffic that are dropped by firewalls. Ports involved were Port 25, 646, 4002, 8899, 12345, etc

The attack surface that can be seen from these come in three different parts:
1. First is the web server. Since the web server port 80   is open, we can use tools like gobuster to reveal hidden directories or if the server is running on an old version that has an exploit then we can use it against.
2. Next is the SSH server running on port 22. Since the version is old, there could be some CVE associated with the version that could be used to exploit. If not, we can brute force if weak credential are suspected
3. Finally the presence of filtered ports means means  we cannot interact with them directly so we can try evading or bypassing the firewall like 
	1. Try to sneak the traffic through allowed ports (like tunneling SSH over Port 443).
	2. Use packet fragmentation to confuse the firewall.
	3. Look for a completely different port that _isn't_ filtered.

---

## Attack Surface Summary: scanme.nmap.org

### 1. Scope and authorization

Target: `scanme.nmap.org` (45.33.32.156). Nmap publishes this host for scan practice and permits port scanning of it. Activity was limited to host discovery, port scanning, service/version detection, and default NSE scripts. No exploitation, brute force, firewall evasion, or denial-of-service testing was performed.

### 2. Method

- Date and time of scans: [date, time, timezone]; source: [my VM / network].
- Commands: `nmap scanme.nmap.org`, `nmap -sV scanme.nmap.org`, `nmap -sC scanme.nmap.org`.
- Default scans check the 1,000 most common TCP ports only. UDP and all 65,535 TCP ports were not scanned.

### 3. Host information

|Item|Result|Basis|
|---|---|---|
|IPv4|45.33.32.156|Observed (DNS, `dig`)|
|Reverse DNS|ack.nmap.org|Observed|
|Operating system|Linux|Inferred from service banners (“Service Info” line); OS detection (`-O`) was not run|

### 4. Open ports and services (observed)

|Port|Service|Detail|
|---|---|---|
|22/tcp|SSH|OpenSSH 6.6.1p1|
|80/tcp|HTTP|Page title “Go ahead and ScanMe!” (from `-sC`)|
|9929/tcp|nping-echo|Nmap’s Nping echo server|

### 5. Filtered ports (observed)

Ports 25, 646, 4002, 8899, 12345 and others returned no conclusive response. Nmap marks these _filtered_, meaning it could not determine whether they are open. This is consistent with a firewall or other network filter but does not identify a specific rule.

### 6. Exposure analysis

1. **SSH (22).** The banner reports OpenSSH 6.6.1p1, which is an older release. _Inferred:_ it may be missing fixes. _Not established:_ distributions often backport patches without changing the banner, so exploitability is unconfirmed until the package version and configuration are checked. Password authentication, if enabled, would add credential-guessing exposure. This was not tested.
2. **HTTP (80).** A web service is reachable. _Not tested:_ hidden content, software version, application flaws. These would need separate authorization on a real target.
3. **Nping echo (9929).** A non-standard service is exposed. On this host that is expected, because it is a purpose-built test target.
4. **Filtered ports.** They show that some ports are not reachable from my vantage point. They are not an exposure by themselves.

### 7. Recommendations (if this were a production host)

- Confirm the installed OpenSSH package version and patch level, then upgrade or document backported fixes.
- Use key-based SSH authentication, disable password login, and restrict SSH by source address where possible.
- Expose only the services that need to be public; close or filter the rest, including test services.
- Keep the web server patched and its banner and default content minimal.

### 8. Limitations

Single scan source and time; default top-1,000 TCP ports only; no UDP, no full-port scan, no authenticated checks. Open or filtered status can change by time, source address, or rate limiting. Findings describe what was observed, not confirmed vulnerabilities.

---

**What makes this 5/5:**

- **Scope and authorization:** There’s a scope statement, and the analysis suggests nothing you weren’t permitted to do.
- **Evidence labels:** Observed and inferred are labeled in separate columns and sentences, so the OS and the OpenSSH age don’t read as facts.
- **Method and limits:** The commands, the date, the top-1,000-ports limit and the scan source are stated.
- **Filtered, not blocked:** “Filtered” is described as unclear, not as dropped by a firewall.
- **Remediation:** It says what the owner would fix, which is what a client reads first.