**Automation Mindset** Scripts exist to eliminate repetitive manual work. Any command you run more than twice is a candidate for automation. Any multi-step process is a candidate for a script.

**Arguments Make Scripts Flexible** Hardcoded filenames make scripts useless outside one situation. Arguments make the same script work on any input. Always design scripts to accept input rather than hardcode values.

**Defensive Scripting** Always check:

- Was an argument provided? (`-z`)
- Does the file exist? (`-f`)
- Does the directory exist (`-d`)
- Did the last command succeed? (`&&`)

Real security tools never assume — they verify every assumption before acting.

**Command Substitution `$()`** Captures the output of a command and stores it as a value. Foundation of dynamic scripting — your script reacts to the current state of the system rather than hardcoded values.

**Security Automation Pattern**

bash

```bash
# The pattern every security tool follows:
# 1. Validate input
# 2. Check environment
# 3. Execute operation
# 4. Report results
# 5. Handle errors
```

Your `log-check.sh` already follows this pattern.

**Functions are reusable mini‑scripts.** They let you encapsulate logic (validation, processing) and call it multiple times. This avoids repetitive code and makes scripts easier to test and maintain.

**Return values signal success/failure.** The convention is 0 for success, non‑zero for failure. Callers use `$?` to make decisions. This is exactly how real security tools (nmap, Metasploit modules, custom scanners) indicate success or failure to automation frameworks.

**Scope matters.** Variables inside a function, including `$1`, refer to the function's arguments, not the script's. This isolation prevents accidental overwrites and makes functions portable across scripts.

**Defensive scripting with loops.** When processing multiple items, use `return` instead of `exit` so one failure doesn't abort the entire batch. Combine with `$?` checks to log errors while continuing through the list — a pattern used in vulnerability scanners and log‑processing pipelines.

### Bash Scripting — Concepts

|Concept|Explanation|
|---|---|
|**Automation Mindset**|Scripts exist to eliminate repetitive manual work. Any command you run more than twice is a candidate for automation. Any multi-step process is a candidate for a script.|
|**Arguments Make Scripts Flexible**|Hardcoded filenames make scripts useless outside one situation. Arguments make the same script work on any input. Always design scripts to accept input rather than hardcode values.|
|**Defensive Scripting**|Always check: Was an argument provided? (`-z`) Does the file exist? (`-f`) Did the last command succeed? (`$?`). Real security tools never assume — they verify every assumption before acting.|
|**Command Substitution `$()`**|Captures the output of a command and stores it as a value. Foundation of dynamic scripting — your script reacts to the current state of the system rather than hardcoded values.|
|**Scope**|Variables inside a function (`$1`) refer to the function's arguments, not the script's. This isolation prevents accidental overwrites and makes functions portable.|
|**Exit Codes**|Programs use exit codes to communicate success (0) or failure (non-zero) to other programs. Security tools like nmap, grep, and Metasploit modules all follow this convention.|
|**Security Automation Pattern**|Every security tool follows: 1. Validate input → 2. Check environment → 3. Execute operation → 4. Report results → 5. Handle errors. Your scripts should too.|
