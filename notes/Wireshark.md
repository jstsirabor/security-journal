# Month 2, Week 3, Day 3 — Wireshark & Packet Analysis (Summary)

## 1. The Mechanics of Capturing (Precision Level)
Before you even click "start", a top-tier engineer understands the environment.

*   **Interface Selection:** Always use `ip a` and look for `state UP` and `LOWER_UP`. Capturing on a `DOWN` or `NO-CARRIER` interface yields zero packets.
*   **Promiscuous Mode (Wired):** Tells the network card to pass all packets up to the OS, not just those addressed to your MAC. 
*   **Monitor Mode (Wi-Fi):** Required to capture raw 802.11 radio frames. Without it, you only see traffic destined for your own Wi-Fi card.
*   **The Visibility Reality:** You cannot casually see other people's passwords on public Wi-Fi because of three walls:
    1.  **WPA2/WPA3 encryption** (scrambles the radio waves).
    2.  **Client Isolation** (routers block devices from talking to each other).
    3.  **Switched networks** (access points only send data to your specific MAC).
*   **Port Mirroring (SPAN):** The professional, silent way to capture an entire network's traffic at the switch level, avoiding the disruption and noise of ARP Spoofing.

## 2. DNS Reconnaissance (Layer 7)
*   **Filter:** `dns`
*   **What we saw:** A UDP packet on **Port 53**. We saw the plaintext query for `sanity-proxy-v2.phantom.app`.
*   **Attacker Mindset:** Even if web traffic is encrypted, DNS is usually plaintext. An attacker sniffing the network can build a profile of the apps and sites you use. They can also perform **DNS Spoofing** (returning a malicious IP) or use **SNI Filtering** to block domains.

## 3. The TCP 3-Way Handshake (Layer 4)
We watched the theoretical OSI model come to life.
*   **Packet 1 (SYN):** Client sends `0x002 (SYN)` to the server.
*   **Packet 2 (SYN-ACK):** Server replies `0x012 (SYN, ACK)`.
*   **Packet 3 (ACK):** Client replies `0x010 (ACK)`.
*   **The Security Proof:** This live capture proves why **IP Spoofing fails for TCP**. The server sends the SYN-ACK to the source IP. A spoofed attacker never receives it, so the handshake dies. IP spoofing is only good for "blind" DoS attacks.

## 4. TLS & SNI (Layer 6)
*   **Filter:** `tls.handshake.type == 1` (Client Hello)
*   **What we saw:** A QUIC (HTTP/3) packet over UDP containing a TLS 1.3 handshake. We were able to read the plaintext domain: `app-proxy.phantom.app`.
*   **The Precision Upgrade:** Because servers host multiple websites, the client must send the **SNI (Server Name Indication)** in plaintext so the server knows which certificate to provide. 
*   **Attacker/Defense Mindset:** Firewalls use SNI filtering to block websites without decrypting the traffic. Defenders are currently rolling out **ECH (Encrypted Client Hello)** to encrypt the SNI.

## 5. ARP & Layer 2 Visibility
*   **Filter:** `arp`
*   **What we saw:** "Who has 192.168.8.195? Tell 192.168.8.1" and "192.168.8.195 is at 48:d2:24:31:ec:7c". You matched your own MAC address from the `ip a` output.
*   **The Precision Upgrade:** MAC addresses are easily spoofed in software (`macchanger`). Therefore, MAC filtering is a weak defense. ARP has zero authentication, which is why ARP Spoofing works.

## 6. The Critical Precision Upgrades (From ChatGPT Corrections)
*   **SSL Stripping Reality:** You cannot just "fake" a lock in a browser. True SSL stripping requires downgrading the connection to HTTP. The browser will **not** show a lock (unless the user clicks through a scary certificate warning). The true defense is **HSTS (HTTP Strict Transport Security)**.
*   **XSS & HttpOnly:** `HttpOnly` stops JavaScript from *reading* the cookie. But XSS is still devastating because the injected script can make authenticated API requests (the browser automatically attaches the cookie to the request).