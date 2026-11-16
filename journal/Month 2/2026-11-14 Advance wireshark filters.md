## Date: 2026-11-14

### What I tried
```
If you ran `curl -X POST http://httpbin.org/post`, here is what almost certainly happened:

1. Your `curl` command sent the request to Port 80 (HTTP).
    
2. `httpbin.org`'s server saw the HTTP request and immediately replied with a **`301 Moved Permanently`** or **`307 Temporary Redirect`**.
    
3. The server forced your `curl` command to reconnect using **HTTPS** (Port 443).
    
4. The actual POST request (with your password) was sent over the encrypted TLS tunnel.
    

So, you _did_ send the password, but the server protected you from yourself by forcing encryption. This is exactly why finding plaintext credentials in the wild is becoming rarer—the internet is slowly forcing everyone into HTTPS.
```
- Base64 is not encryption. It is **encoding**. Imagine you have a fragile glass vase, but you are only allowed to mail standard-sized cardboard boxes. So, you carefully pack the vase into a standard box. Base64 takes binary or complex data and translates it into plain text letters and numbers (A-Z, a-z, 0-9, +, /) so it can be easily transmitted. Anyone can unpack it; it's not a secret, it's just a different format.
	- The command is `cat data.txt | base64 -d` where `-d` is the flag for decode
- `tr` (translate) takes two sets of characters and swaps them.  The syntax is: `tr 'SET1' 'SET2'`. For ROT13, you need to rotate the alphabet by 13 places.
	- The first 13 letters (A-M) map to the last 13 letters (N-Z).  
	- The last 13 letters (N-Z) map back to the first 13 letters (A-M).
	- So for **uppercase**, the mapping is: `A-Z` to `N-ZA-M`.  
	For **lowercase**, the mapping is: `a-z` to `n-za-m`.
	To tell `tr` to handle _both_ uppercase and lowercase at the same time, we just put them right next to each other in the quotes:
	- **Set 1:** `A-Za-z`
	- **Set 2:** `N-ZA-Mn-za-m`
- **`cp` vs `mv`:** When a directory is read-only (like the Bandit home directories), you can't move files out, but you can copy them.
- **File Extensions Matter:** Tools like `gzip` and `bzip2` care deeply about file extensions. If a tool complains about an "unknown suffix," just `mv` the file to the correct extension.
- **`file` is your best friend:** Never guess what a file is. Look at the magic bytes.

---
- ### 📝 Bandit Level 11: ROT13 Cipher (Character Translation)

- **The Challenge:** Decode a string where all letters have been rotated by 13 positions.
    
- **The Tool:** `tr` (Translate).
    
- **The Command:** `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
    
- **How it Works:**
    
    - `tr` maps characters from the first set to the second set.
        
    - `A-Z` maps to `N-ZA-M` (because rotating `A` by 13 gives `N`, and rotating `M` by 13 wraps around to `Z`).
        
    - `a-z` does the exact same thing for lowercase letters.
        
- **Top 1% Lesson:** `tr` is a powerful tool for quick character substitution. It's often used in CTFs for ROT13, but also by attackers to bypass basic text filters (e.g., replacing spaces with tabs, or filtering out specific characters).

---

### 📝 Bandit Level 12: The Russian Nesting Doll (Decompression)

- **The Challenge:** A hex dump file that has been compressed, archived, and renamed multiple times.
    
- **The Workflow:** You must reverse the hex dump, identify the file type, and use the correct decompression tool, peeling back one layer at a time.
    
- **The Commands:**
    
    - `xxd -r data.txt > data.bin` (Reverses the hex dump into binary).
        
    - `file data.bin` (Your most important tool—identifies the file format).
        
    - `mv data.bin data.gz` (Renames the file because `gzip` demands a `.gz` extension).
        
    - `gzip -d data.gz` (Decompresses gzip).
        
    - `bzip2 -d data.bz2` (Decompresses bzip2).
        
    - `tar -xf data.tar` (Extracts a tar archive).
        
- **Top 1% Lessons:**
    
    1. **Read-Only Directories:** You cannot `mv` files out of the Bandit home directory. You must `cp` them to a writable directory like `/tmp` first.
        
    2. **Tools are picky:** `gzip` and `bzip2` will fail with an "unknown suffix" error if the file doesn't have the correct extension. Always check the extension.
        
    3. **The Loop:** Never assume the next layer. Always run `file` after every extraction to see what you are dealing with next.
        

---

### 📝 Bandit Level 13: SSH Keys & Localhost Restrictions

- **The Challenge:** Read a password file you don't have permission to read, using a provided SSH private key.
    
- **The Obstacle:** You tried to SSH from `bandit13` to `bandit14` on the same server, but Bandit blocks `localhost` SSH connections to conserve resources.
    
- **The Solution:** Download the key to your _local_ machine and connect from there.
    
- **The Commands:**
    
    - `scp -P 2220 bandit13@bandit.labs.overthewire.org:~/sshkey.private .` (Downloads the key to your local machine).
        
    - `chmod 600 sshkey.private` (Secures the key so only your user can read it).
        
    - `ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220` (Logs in using the key).
        
    - `cat /etc/bandit_pass/bandit14` (Reads the password now that you are bandit14).
        
- **Top 1% Lessons:**
    
    1. **SSH Permission Strictness:** SSH will refuse to use a private key if it is readable by anyone else. `chmod 600` is mandatory.
        
    2. **`scp` uses uppercase `-P`:** While `ssh` uses lowercase `-p` for the port, `scp` uses uppercase `-P`. (A classic Linux gotcha).
        
    3. **Pivoting:** When a server blocks you from attacking itself (localhost restriction), you "pivot" to your host machine to launch the connection. This is a core penetration testing concept.
### What broke
-

### What I learned
- In Wireshark, you can filter for specific TCP flags. 
- `tcp.flags.syn == 1` tells Wireshark: "Ignore everything except packets where the SYN (Synchronize) flag is set to 1." This is used  to:
	- see what servers people on the network are trying to reach
	- see if a server is being scanned - a port scan sends a massive flood of SYN packets to different ports
	- If an attacker is doing an ARP spoofing attack, they want to see who  is initiating connections so they know who is actively browsing 
	- They see a list of every computer trying to open a connection.
    - They see the exact **Destination IP** and **Port** (e.g., Port 80, Port 443, Port 22).
    - **The Attack:** If the attacker sees you sending a SYN packet to `192.168.1.50` on Port 22, they now know there is an SSH server on the network. They know exactly where to point their attack. This filter is pure **Reconnaissance**.
- The next filter is `http`
	- In HTTP, there is no encryption. If an attacker is sniffing the wi-fi, they could read what website the computer is talking to, and what data it's sending.
- 
1. **`http` (Port 80):** The Holy Grail. If traffic is unencrypted, the attacker reads the exact `GET` or `POST` requests. They see usernames, passwords, API keys, and exactly what pages you are visiting.
2. **`dns` (Port 53):** The Phonebook. Even if the website is encrypted, DNS is usually plaintext. The attacker sees the domain you are looking for (e.g., `phantom.app`). They can build a profile of your apps or perform a DNS Spoofing attack.
3. **`tls.handshake.type==1` (Client Hello):** The SNI. Even if the traffic is encrypted, the attacker reads the plaintext domain name on the outside of the "sealed safe". They know exactly which HTTPS website you are visiting.
4. **`tcp.flags.syn == 1` (The Handshake):** Reconnaissance. By looking only at connection attempts, the attacker sees which internal servers and ports are alive (e.g., "Ah, they are trying to connect to Port 22, there must be an SSH server there").

```
	# Month 2, Week 3, Day 4 — Wireshark Filters & Attacker Mindset

### 1. The `tcp.flags.syn == 1` Filter (Reconnaissance)
*   **The Analogy:** Imagine a massive concert where thousands of people are inside dancing (normal traffic). You are a security guard who only cares about the exact moment a new person walks up to the ticket booth and says, "I want to come in."
*   **The Technical Breakdown:** This filter ignores all data packets and only shows the very first step of the 3-way handshake (the SYN packet). It shows you every time a computer tries to start a new connection.
*   **The Attacker Mindset:** An attacker uses this filter to see what servers and ports people on the network are trying to reach. If the attacker sees you sending a SYN packet to an internal IP on Port 22, they now know an SSH server exists there. It is pure **Reconnaissance**.

### 2. The `http` Filter (The Holy Grail)
*   **The Technical Breakdown:** Filters for Port 80 (unencrypted web traffic).
*   **What we saw:** You successfully captured a `GET / HTTP/1.1` request from your computer to Ubuntu's connectivity check server. Because it was HTTP, the bottom-right pane of Wireshark showed the plaintext request (like reading a postcard instead of a sealed letter).
*   **The Attacker Mindset:** This is the ultimate goal for an attacker. If a website uses HTTP, the attacker can read exact `GET` and `POST` requests, extracting usernames, passwords, and API keys.

### 3. The `curl` Experiment (The Modern Reality Check)
*   **What we tried:** We used `curl` to send a fake username and password (`admin` / `supersecret123`) to an HTTP endpoint.
*   **What happened:** The password didn't show up in plaintext. 
*   **The Precision Upgrade:** The server responded with a **Redirect (301/307)**. It forced the `curl` command to reconnect using HTTPS (Port 443) before accepting the data. 
*   **The Lesson:** Finding plaintext credentials in the wild is becoming rare. Modern web servers actively protect users by forcing encryption (HTTPS) and using **HSTS (HTTP Strict Transport Security)** to prevent downgrade attacks. 

---

### The Attacker's Mindset Checklist (The 4 Filters)

If you are intercepting traffic (via ARP Spoofing or Port Mirroring), here is exactly what you learn from each filter:

1.  **`dns`**: The Phonebook. Reveals exactly which domains the victim is trying to reach (e.g., `phantom.app`).
2.  **`tcp.flags.syn == 1`**: The Ticket Booth. Reveals which internal servers, ports, and services are alive (Reconnaissance).
3.  **`tls.handshake.type == 1`**: The SNI. Reveals the domain name of the HTTPS site being visited, even though the traffic is encrypted.
4.  **`http`**: The Holy Grail. Reveals plaintext data, credentials, and cookies if the site is unencrypted.
```
- `tcp.flags.syn == 1` shows packets with the SYN flag set, including SYN-ACK packets. To isolate only initial connection attempts, use `tcp.flags.syn == 1 && tcp.flags.ack == 0`.
- `http` filters for traffic Wireshark recognizes as HTTP; it is not simply “port 80.” Likewise, a redirect to HTTPS is useful protection, while HSTS is the separate browser policy that prevents future HTTP downgrade attempts after being received securely or via a preload list.
- Without DNS, we'd have to  memorize the IP address of every website we wanna visit
- `dig` (Domain Information Groper) is the command-line tool used to  query the DNS operator
- The most fundamental DNS record is the A record which maps a domain name to an IPv4 address. It basically tells the street address/building for a website
	- dig scanme.nmap.org A -> This shows the IP address in the answer section
- There's also the MX record (Mail Exchange) which tells where the mailroom is. If a company uses a third-party service like Google workspace or Microsoft 365 to hndle their email, their web server (A record) will have a completely different IP address than their mail server
	- dig scanme.nmap.org MX -> if there is no mail server, the answer section would be empty
	- The authority section shows the NS Records (Name Server records) which  tells which  servers are officially in charge of holding the DNS records for this domain. If an attacker can compromise those authoritative name servers, they can change where the whole domain points. This is known as DNS hijacking attack
- We also  have the TXT records which is basically a public bulletin board where a domain owner can leave text notes.
	- Why do security people care? Because of **SPF (Sender Policy Framework)**. SPF is a TXT record that says: _"Here is a list of the ONLY servers allowed to send email on behalf of my domain."_
	- If a domain doesn't have an SPF record, attackers can easily spoof their email address (spam, phishing).
- `nmap` (Network Mapper) is an automated building inspector. It runs down the hallway and knocks on every door, writing down which ones are open and what service is running behind them.
- `nmap.org` uses a **Wildcard DNS record**. It basically says, _"Any random subdomain you type (like `scname` or `blahblah`), I will just point to this same IP address."_ Attackers look for wildcard DNS all the time, because it can sometimes reveal hidden internal systems.
```
Not shown: 997 filtered tcp ports (no-response) 
PORT STATE SERVICE 
22/tcp open ssh 
113/tcp closed ident 
443/tcp open https
```
- Open means the server is actively listening and accepting connections on these ports
- Closed means the server received the request but there is no service actively listening on that port
- filtered means a firewall or router is silently dropping the packets. The server never replied to Nmap's knock. It's a black hole
- Nmap has a flag called `-sV` (Service Version detection). When you use it, Nmap doesn't just knock on the door; it peeks inside and asks, _"Hello, what software and version are you running?"_. This could help know if the port is running an old, vulnerable version or a modern, patched one. 
- Attackers don't guess, they google. If i run a version scan and the version has a known vulnerability (a CVE), then I know that the server is a target.
- What is `tcpwrapped`? It means Nmap knocked on the door, the server answered the TCP handshake, but then immediately closed the connection before Nmap could ask for the version. This usually means a firewall (like TCP Wrappers) is protecting that port, or it only accepts connections from specific IPs.
- One more flag is **`-sC`**: This runs the Nmap Scripting Engine (NSE). It launches a series of safe, automated scripts that ask the server for more information—like grabbing the SSH host key or checking HTTP headers.
### Commands/code worth remembering
```code

```

### Questions for later
-