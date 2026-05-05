**Vim — Essential Commands**

|Command|Action|
|---|---|
|`vim filename`|Open file|
|`i`|Enter insert mode (start typing)|
|`Escape`|Return to normal mode|
|`:w`|Save|
|`:q`|Quit|
|`:wq`|Save and quit|
|`:q!`|Quit without saving|
|`/word`|Search for word|
|`n`|Jump to next search result|
|`dd`|Delete current line|

Run `vimtutor` to practice interactively.

**Nano — Quick Reference**

|Shortcut|Action|
|---|---|
|`Ctrl+O`|Save|
|`Ctrl+X`|Exit|
|`Ctrl+W`|Search|
|`Ctrl+K`|Cut line|
|`Ctrl+U`|Paste|

---

**Bash Scripting Fundamentals**

**The Shebang**

bash

```bash
#!/bin/bash
```

First line of every script. Tells the system which interpreter to use. Without it, the system doesn't know what language the script is written in.

**Comments**

bash

```bash
# This is a comment — ignored by bash, read by humans
```

Always comment your scripts. Your future self will thank you.

**Making a Script Executable**

bash

```bash
chmod 755 myscript.sh    # give execute permission
./myscript.sh            # run it
```

**Variables**

bash

```bash
NAME="Alice"             # store a value
echo "$NAME"             # use the value with $
DATE=$(date)             # command substitution — captures command output
USER=$(whoami)           # stores result of whoami in USER
```

**Arguments**

bash

```bash
$1    # first argument passed to script
$2    # second argument
$@    # all arguments
```

Example: `./script.sh file.txt` → `$1` = `file.txt`

**Conditionals**

bash

```bash
if [ condition ]; then
    # runs if true
else
    # runs if false
fi
```

**Common Conditions**

|Condition|Meaning|
|---|---|
|`[ -f "file" ]`|File exists|
|`[ -z "$VAR" ]`|Variable is empty|
|`[ "$A" == "$B" ]`|A equals B|
|`[ "$A" != "$B" ]`|A does not equal B|

**Exit Codes**

bash

```bash
exit 0    # success
exit 1    # error
```

Programs use these to communicate success or failure to other scripts.

**Flags**

|Flag|Meaning|
|---|---|
|`-y`|Yes to all confirmations — keeps scripts running unattended|
|`&&`|Run second command only if first succeeds|
