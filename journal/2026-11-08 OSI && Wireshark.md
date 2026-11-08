## Date: 2026-11-08

### What I tried
```
You said: _"They could find the session cookies to gain access to the active session."_

This is 100% correct. But let's apply the "Attacker Mindset" precision upgrade. If the traffic is truly encrypted with HTTPS (TLS), the attacker at Layer 2 sees only scrambled data. **So how do they get the cookie if it's encrypted?**

1. **SSL Stripping (Layer 6 Attack):** The attacker intercepts the HTTPS request and downgrades it to HTTP before it reaches the server, and downgrades the response back to HTTPS before it reaches the victim. The victim thinks they are on a secure site (because their browser shows the lock), but the connection between the victim and the attacker is unencrypted. The attacker reads the cookie in plaintext.
    
2. **Missing `Secure` Flag:** If the web application is poorly coded and doesn't set the `Secure` flag on the cookie, the browser might accidentally send the cookie over an unencrypted HTTP request (like loading an image on the page). The attacker intercepts that unencrypted request and steals the cookie.
    
3. **Cross-Site Scripting (XSS):** If the attacker injects JavaScript into the page, the script can read the cookie directly from the browser's memory (unless the cookie is marked `HttpOnly`).
    

**The Lesson:** Encryption (HTTPS) is mandatory, but it is not magic. If the application has flaws, or if the cookie flags aren't set correctly, the attacker can still find a way to steal the session.
```
- A local attacker cannot make a browser show a valid HTTPS lock merely by using HTTPS between themselves and the victim. Proper certificate validation would expose that interception. Classic SSL stripping works only when a victim begins on HTTP and the site does not force HTTPS with HSTS; the victim should see HTTP—not a valid secure connection. Likewise, `HttpOnly` stops injected JavaScript from directly reading a cookie, though XSS can still be devastating because it can act within the victim’s session.
```
### The Precision Upgrade: How SSL Stripping Actually Works

You are right: an attacker **cannot** just use HTTPS with the victim and magically get a valid lock. If an attacker tries to serve `https://bank.com` to the victim using their own fake certificate, the victim's browser will throw a massive, scary warning: _"Your connection is not private."_ Most users will stop there.

Here is how **actual** SSL Stripping (like the famous `sslstrip` tool) works:

1. The victim types `http://bank.com` (or clicks an HTTP link). **There is no lock, because it's HTTP.**
    
2. The attacker intercepts this HTTP request.
    
3. The attacker connects to the real `https://bank.com` on the backend.
    
4. The bank replies over HTTPS to the attacker. The attacker decrypts it, and sends the data back to the victim over **HTTP**.
    
5. The victim is looking at an HTTP page. **They do not see a lock.** They see a blank page or an insecure connection. But the attacker is feeding them the real page content, so they don't notice.
    

**The Defense: HSTS (HTTP Strict Transport Security)**  
This is the missing piece I left out. HSTS is a header the server sends that tells the browser: _"Never, ever connect to me over HTTP. Always use HTTPS."_ The browser remembers this. If an attacker tries to downgrade the connection to HTTP, the browser refuses to load the page at all. That is how modern websites defeat SSL stripping.

---

### The Precision Upgrade: XSS and HttpOnly

You are also right about the XSS and `HttpOnly` distinction.

I said: _"If the attacker injects JavaScript... it can read the cookies directly (unless the cookie is marked HttpOnly)."_

ChatGPT's correction is perfect: **If the cookie is `HttpOnly`, the JavaScript cannot read it.** But XSS is still devastating. Why?

Because the attacker doesn't need to _read_ the cookie; they just need to _use_ the browser.  
If the attacker injects JavaScript, that script runs inside the victim's browser. The script can say: `fetch('/api/transfer-money?to=attacker')`. The browser will automatically attach the `HttpOnly` session cookie to that request because the browser handles the cookie, not the JavaScript.

**The Lesson:** `HttpOnly` stops cookie theft. It does **not** stop the attacker from acting as the user through the victim's own browser.
```
- Seeing ARP in wireshark is the computer actively asking the local network, "who has this IP address? Tell me your MAC address" - Layer 2 -> Data link
- DNS is the computer asking the internet, "What is the IP address for this website?" - Layer 7 -> Presentation
- TCP is the transport layer establishing connection - Layer 4 -> Transport layer
- TLSv1.2 and TLSv1.3 is the encryption (HTTPS). Is shows the handshake that establishes a secure connection. It is the protocolthat encrpyts your web traffic
- QUIC -? This is a modern protocol buikt on top of UDP. It's how modern apps and browsers talk to the internet faster
- MDNS and IGMPv3 is about network descovery - printers, chromecasts etc
- ICMPv6 is about IPv6 network diagnotstics like ping
- Most websites nowadays use HTTPS (TLS) and not HTTP
- Port 53 is the universal port for DNS
- If an attacker is sniffing traffic on the local network, they don't need to know the password to learn about you. If they see that you using Phanom (a crypto wallet), it is called network reconnaissance.
- Since DNS is sent over UDP which is unencrypted by default, an attacker can perform DNS spoofing - meaning replying with a fake IP address to send you a malicious website that looks exactly like phantom
```
Look at the details in your screenshot. You are looking at the absolute first step of the TCP 3-way handshake. Here is the top 1% breakdown of what your computer just did:

- **Source IP:** `192.168.8.195` (You)
- **Destination IP:** `192.168.207.159` (The server)
- **Source Port:** `54328` (Your computer picked a random high-numbered port to talk from)
- **Destination Port:** `33455` (The port the server is listening on)
- **Flags:** `0x002 (SYN)`
- **Seq: 0, Ack: 0**
    
Your computer is saying: _"Hello server, I want to talk to you. Let's synchronize. My starting sequence number is 0."_ No data has been sent yet (`TCP Segment Len: 0`).
```

```
QUIC is HTTP/3. It's the modern protocol used by Google, Facebook, and many apps. It runs over UDP to be faster, but it still needs encryption. So, the TLS handshake happens _inside_ the QUIC packet. You just captured a QUIC connection performing a TLS 1.3 handshake.

**Why can you see `app-proxy.phantom.app` if it's encrypted?**  
Because of the **SNI (Server Name Indication)**. When a server hosts multiple websites (like a shared hosting provider or a CDN), the client has to tell the server _which_ website it wants _before_ the encryption keys are exchanged. If the SNI were encrypted, the server wouldn't know which SSL certificate to present.

So, the Client Hello is sent in plaintext.

**The Attacker Mindset:**  
If an attacker is sniffing your traffic, they can't see _what_ you are doing inside the encrypted tunnel, but they can see _who_ you are talking to by reading the SNI.

- **Defense (ESNI/ECH):** The industry created ECH (Encrypted Client Hello) to encrypt the SNI so attackers can't even see the domain name. But it's not fully deployed yet.
    
- **Attack (SNI Filtering):** Firewalls can block traffic based on the SNI. (e.g., A company firewall blocking `facebook.com` just by reading the Client Hello, without decrypting the traffic).
```
### What broke
-

### What I learned
- Layers 5, 6 and 7 blend together into The Application.
	- Layer 5 is the session layer which manages the conversation keeping you  logged in
	- Layer 6 is the presentation layer which translates data (like encryption/decryption) e.g SSL/TLS
	- Layer 7 is the application layer where the actual user-facing protocols live e.g HTTPS, DNS, FTP, SSH and SQL
	- The attack surface is usually the layer 7 - application layer because layers 1-4 are usually locked down by firewalls and routers but layer 7 is the actual application written by humans, full of logic flaws and unvalidated input. They include:
		- SQL Injection(SQLI) involves trickingt he database into running your commands
		- Cross-Site Scripting(XSS) involves tricking a iser's browser into running your code
		- Prompt injection in AI security involves tricking an AI model into ignoring its instructions
	- If an attacker steals your session cookie, they don't need your password; they just take over your active session.
- A firewall protects the _doors_ (ports) and the _street address_ (IP), but it does not read the _letter_ inside the envelope. If the web application (Layer 7) is vulnerable to SQL injection, the firewall will happily let the malicious SQL payload through Port 443.
- **SSL Stripping:** Works by downgrading HTTPS to HTTP. The victim does _not_ see a lock (unless the attacker tricks them into accepting a bad certificate). Defended by **HSTS (HTTP Strict Transport Security)**.
- **XSS & HttpOnly:** `HttpOnly` prevents JavaScript from reading the cookie. However, XSS is still critical because the injected script can make authenticated API requests (the browser attaches the cookie automatically).
```
Here is what a top 1% engineer knows before they even open Wireshark:

### 1. The Engine Under the Hood (`libpcap` / `BPF`)

Wireshark is just a GUI. The actual capturing is done by a library called `libpcap` (on Linux). It uses **BPF (Berkeley Packet Filter)** in the Linux kernel. This is crucial: **you can filter traffic _before_ it ever hits your CPU**. If you are on a 10 Gigabit network, you cannot capture everything and filter it in the GUI—your machine will crash. You must use BPF to tell the kernel: _"Only send me TCP packets on port 443."_

### 2. The "Switched Network" Reality

In old networks (hubs), every computer saw every packet. Modern networks use **switches**. A switch builds a MAC table and sends traffic _only_ out of the specific port where the destination MAC address lives.  
**The Top 1% Catch:** If you just start Wireshark on your laptop, you will only see **your own traffic** (broadcasts, your requests, etc.). You will _not_ see your roommate's traffic. To see others' traffic, you need either:
- Port Mirroring (SPAN) configured on the switch by an admin.
- An ARP Spoofing attack (which we just learned) to force their traffic through your machine.
    

### 3. Promiscuous Mode vs. Monitor Mode

- **Promiscuous Mode:** For wired Ethernet. Tells the network card to pass _all_ packets it receives up to the OS, not just the ones addressed to your MAC.
- **Monitor Mode:** For Wi-Fi. You can't just use promiscuous mode on Wi-Fi; you have to put the card into Monitor Mode to capture the raw 802.11 radio frames (including beacon frames from access points and unencrypted data).
```
- `ip a` is the command to find my network interface
```
**`enp3s0`** says: `<NO-CARRIER,BROADCAST,MULTICAST,UP> state DOWN`  
**`wlp2s0`** says: `<BROADCAST,MULTICAST,UP,LOWER_UP> state UP`

**What this means:** `enp3s0` is your Ethernet port. `NO-CARRIER` and `state DOWN` means there is no cable plugged into it. `wlp2s0` is your Wi-Fi card, and it is `UP`.

This is a top 1% detail. If you start Wireshark on `enp3s0`, you will capture absolutely zero traffic. You must capture on `wlp2s0`.
The state tells you which one to choose
```

```
Imagine you are a network admin and you want to capture traffic on a switch. You have two choices:

1. **ARP Spoofing:** You pretend to be the router. All the computers send their traffic through your laptop.
    - **The Problem:** It's an active attack. You are disrupting the network. If your laptop crashes, the whole network goes down. It's loud, and security systems will immediately flag you.
        
2. **Port Mirroring (SPAN):** You log into the switch and tell it: _"Take a copy of all traffic on Port 1 and send it to Port 24."_ You plug your laptop into Port 24.
    - **The Advantage:** It is silent and passive. The network runs perfectly. Nobody knows you are watching.
        

**The Lesson:** As an attacker, you use ARP spoofing to be disruptive and intercept live traffic. As a defender/analyst, you use Port Mirroring to monitor the network silently.
```

```
### Why you can't see other people's passwords on Coffee Shop Wi-Fi??

Here are the **three walls** that stop you:

**1. The Wi-Fi Encryption (WPA2/WPA3)**  
When you connect to a coffee shop Wi-Fi, the traffic is encrypted at Layer 2 using a key derived from the Wi-Fi password. Even if you capture the raw radio waves, Wireshark will just show you scrambled data.

**2. Client Isolation (AP Isolation)**  
Most public Wi-Fi networks have a setting turned on called "Client Isolation." This tells the router: _"Do not allow devices on this Wi-Fi to talk to each other. They can only talk to the internet."_ If this is on, you can't even ping the person next to you, let alone ARP spoof them.

**3. Switched Networks (The Access Point)**  
Just like wired networks, Wi-Fi access points use MAC address tables. They only send your data to _your_ MAC address. Your laptop physically cannot hear the radio waves meant for someone else's laptop unless you put your card into **Monitor Mode** (which is advanced and requires specific hardware).
```
### Commands/code worth remembering
```code

```

### Questions for later
-


```
### Wireshark Lab: Capturing the OSI Model in the Wild

**1. Interface Selection**

- Before capturing, run `ip a`. Look for `state UP` and `LOWER_UP`.
    
- If the interface says `DOWN` or `NO-CARRIER`, there is no traffic flowing. Always capture on the active interface (e.g., `wlp2s0` for Wi-Fi).
    

**2. The Visibility Reality (Why we can't see others' traffic)**

- On modern networks, you cannot casually see other people's traffic because of **Client Isolation** (on public Wi-Fi), **WPA2/WPA3 encryption** (radio waves are scrambled), and **Switched MAC tables** (the access point only sends data to your specific MAC address).
    

**3. DNS Reconnaissance**

- **Protocol:** UDP Port 53 (Unencrypted).
    
- **Attacker Mindset:** Attackers sniffing the network can read your DNS queries in plaintext. They can see exactly what websites or apps you are connecting to (e.g., seeing a query for a crypto wallet app). This can also lead to **DNS Spoofing** (returning a fake IP).
    

**4. The TCP 3-Way Handshake (Live)**

- **Step 1 (SYN):** Your computer (random high port) sends `0x002 (SYN)` to the server. _"Let's talk."_
    
- **Step 2 (SYN-ACK):** The server replies with `0x012 (SYN, ACK)`. _"I hear you, let's talk."_
    
- **Step 3 (ACK):** Your computer replies with `0x010 (ACK)`. Connection established.
    
- **The Security Connection:** This live capture proves why **IP Spoofing fails for TCP connections**. Because the server sends the `SYN-ACK` to the source IP of the `SYN`, a spoofed attacker never sees Step 2, and the handshake dies. This is why IP spoofing is only useful for "blind" attacks like DoS.
```