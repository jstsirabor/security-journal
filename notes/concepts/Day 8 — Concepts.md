**UID 0 is root, not the name.** The kernel identifies users by numeric UID. An account named `bob` with UID 0 is effectively root. Attackers sometimes create hidden root accounts with innocent-looking names to maintain persistence.

**sudo -l reveals every possible privilege escalation path.** After compromising a user, this is the first reconnaissance command. Every `NOPASSWD` entry must be audited — a single writable script or a single hijackable command is a direct path to root.

**The adm group is a silent intelligence tool.** It allows reading authentication logs without root. An attacker can enumerate users, identify trust relationships, and potentially find leaked credentials — all without triggering privilege escalation alerts.

**Groups represent inherited permissions.** Membership in groups like `docker`, `vboxusers`, or `dip` grants capabilities that may not be obvious from the username alone. Always audit group membership when assessing a compromised account.