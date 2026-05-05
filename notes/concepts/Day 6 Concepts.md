**Automation Mindset** Scripts exist to eliminate repetitive manual work. Any command you run more than twice is a candidate for automation. Any multi-step process is a candidate for a script.

**Arguments Make Scripts Flexible** Hardcoded filenames make scripts useless outside one situation. Arguments make the same script work on any input. Always design scripts to accept input rather than hardcode values.

**Defensive Scripting** Always check:

- Was an argument provided? (`-z`)
- Does the file exist? (`-f`)
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