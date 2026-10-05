# AI Security Engineer Roadmap – Learning Journal

**Progress:** Month 1 of 31 complete

This repository documents my structured, 31-month journey from beginner to AI Security Engineer. It contains daily journal entries, lab write-ups, scripts, and notes from following a hands-on roadmap covering Linux, networking, security, and AI/ML systems.

## 🎯 Purpose

- Track daily progress and reflections.
- Build a public record of hands-on skills (not just theory).
- Serve as a portfolio for future employers and collaborators.

## 🗂️ Repository Structure

- `journal/` – Daily entries (what I tried, what broke, what I learned).
- `labs/` – Structured lab reports and investigation write-ups, organized by month.
- `notes/` – Reference material.
- `tools/` – Scripts I wrote.
- `README.md` – This file.

## 📚 What I've Covered So Far (Month 1)

- **Linux Fundamentals:** File system navigation, users, groups, permissions (`chmod`, numeric and symbolic), SUID, processes.
- **Command-Line Tools:** `grep`, `find`, `awk`, `sed`, `cut`, `sort`, `uniq`, `xargs`, `wc`, `tee`.
- **Redirection & Pipes:** `>`, `>>`, `<`, `|`, `2>/dev/null`, `2>&1`.
- **Text Editors:** `nano`, `vim` (completed `vimtutor`).
- **Process Management:** `ps aux`, `htop`, `kill`, `killall`.
- **Network Investigation:** `ss`, `netstat`, `lsof`.
- **Security Concepts:** Sticky bit, `$PATH` hijacking, reverse shells, log analysis, timestomping, alias persistence, binary integrity (`dpkg -V`).
- **Wargames:** OverTheWire Bandit levels 0–5.
## 🔬 Labs

- [Compromised Server Investigation](labs/Month%201/compromised-server-investigation.md) — Log analysis, reverse shell detection, and incident response in a mock environment.

## 🔍 Key Takeaways

- **Consistency over intensity:** Showing up daily (even for 30 minutes) builds more skill than occasional marathon sessions.
- **Security is about connections:** Linking log entries to files (e.g., an attacking IP and a reverse shell) tells the real story.
- **Document everything:** Writing journal entries forces me to articulate *why* something works, which deepens understanding.
- **Verify, don't assume:** Reading about a command is not the same as running it, breaking it, and fixing it.

## 🚧 What's Next

- **Linux Fundamentals II + Networking:** OSI model, Wireshark, `nmap`, `dig`, `cron`, `sudo`, Bandit 6–15.
- **Python Core:** Syntax, data structures, functions, error handling.
- **Python for Security:** Build real tools (log analyzer, header checker, port scanner).
- **Cloud Foundations (AWS):** IAM, S3, EC2, VPC.
- **Web Fundamentals + Docker:** Burp Suite, DVWA, container security.

## 📖 Learning Resources

- **Roadmap:** Custom 31-month AI Security Engineer roadmap (Linux → Networking → Python → Cloud → Web → AI/ML Security).
- **Labs:** OverTheWire Bandit, deliberately vulnerable VMs (DVWA later).
- **Environment:** Linux Mint host, Ubuntu 22.04 VM in VirtualBox, Kali Linux VM.
- **Primary tools so far:** `grep`, `find`, `awk`, `sed`, `cut`, `sort`, `uniq`, `xargs`, `ss`, `lsof`, `nano`, `vim`.

## 📬 Contact

- GitHub: [@jstsirabor](https://github.com/jstsirabor)
- LinkedIn: [Justus Irabor](https://www.linkedin.com/in/justus-irabor)

---

*All work is conducted in authorized, controlled lab environments.*