**Navigation Commands**

- `pwd` — shows your current location in the filesystem
- `ls` — lists files and folders in current location
- `ls -l` — detailed list with permissions, owner, size, date
- `ls -la` — same but includes hidden files (dot files)
- `cd Documents` — move into Documents folder
- `cd ..` — move up to parent directory
- `cd ~` — jump to your personal home directory
- `cd /` — jump to root of entire filesystem

**Key Concepts**

- Dot files (`.bashrc`, `.profile`) are hidden by default — not for security, but to keep file views clean and protect personal configuration from accidental deletion
- `.bashrc` runs automatically every time you open a terminal — contains aliases, environment variables, custom prompt settings
- Hidden = configuration, not necessarily sensitive

**Directory Map**

|Directory|Purpose|Security Relevance|
|---|---|---|
|`/`|Root — top of entire filesystem|Everything lives here|
|`/etc`|System configuration files|Passwords, network settings, service configs|
|`/home`|Personal user directories|Your files, scripts, dot files|
|`/var/log`|Log files|Authentication events, attack evidence|
|`/tmp`|Temporary files|Writable by everyone — attackers drop tools here|
|`/usr/bin`|Everyday user tools|Python, curl, wget — attacker living-off-the-land|
|`/bin`|Essential survival programs|Bare minimum to boot and repair the system|

**Living off the land** — attackers use tools already on the system (`python3`, `curl`, `nc`) rather than bringing their own, because existing tools are less detectable.