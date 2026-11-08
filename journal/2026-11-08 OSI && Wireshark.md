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