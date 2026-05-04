**The Attacker's First 60 Seconds** After gaining access, attackers immediately run:

bash

```bash
id && sudo -l          # Who am I? What can I do?
ps aux | grep root     # What root processes can I target?
ss -tulnp             # What internal services are reachable?
```

Build the picture first. Attack second.

**Credentials in Process Arguments** Developers sometimes pass passwords as command line arguments — visible to anyone who runs `ps aux`. This is a real misconfiguration found in production environments.

**Internal Services — Hidden Attack Surface** Services bound to `127.0.0.1` are invisible from outside the network but reachable from inside. An attacker already inside the system can reach these services — databases, admin panels, internal APIs — that defenders assumed were protected.

**Port-Specific Investigation**

bash

```bash
lsof -i :3306    # Who is using MySQL?
lsof -i :22      # Who is connected via SSH right now?
```

Drill into specific ports instead of reading hundreds of lines.

**Active vs Listening**

- Listening = door exists, nobody walking through yet
- Active connection = someone is currently connected Knowing who is actively connected tells an attacker if an admin is watching — and tells a defender if something unexpected is communicating.