
| Concept              | Meaning                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| SUID                 | File runs as its owner, not the person executing it                    |
| Privilege escalation | Moving from low-privilege user to root by exploiting misconfigurations |
| 600                  | Owner only — for sensitive files like SSH keys                         |
| 755                  | Owner full, everyone else read+execute — for shared tools              |
| 777                  | Everyone full access — almost always dangerous                         |

**Principle of Least Privilege** Every user, file, and process should have exactly the permissions it needs — nothing more. This is the foundation of Linux security and later AWS IAM security.

**SUID (Set User ID)**

- Indicated by `s` in the owner execute position: `-rwsr-xr-x`
- Makes a file run as its **owner** regardless of who executes it
- Example: `/usr/bin/passwd` is owned by root with SUID set — when any user runs it, it executes as root so it can write to `/etc/shadow`
- Dangerous when misconfigured — if a root-owned SUID binary can be manipulated, an attacker gains root access

**Privilege Escalation** Moving from a low-privilege user account to root by exploiting misconfigurations — SUID binaries are one of the most common paths. This is one of the first things attackers attempt after initial access.

**Key Security Rules**

- SSH keys → always `600` — only owner can read, nobody else touches it
- Shared tools → `755` — everyone can use but not modify
- Never use `777` — violates CIA triad, removes all access control
- SUID binaries → audit them with `find /usr/bin -perm -4000 2>/dev/null`

`gtfobins.github.io` — documents every Linux binary that can be abused for privilege escalation.