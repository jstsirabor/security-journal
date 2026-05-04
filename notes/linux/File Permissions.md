**Reading the Permission String**

```
-rw-r--r-- 1 alice staff 1234 Jan 1 myfile.txt
```

|Position|Meaning|
|---|---|
|First character|File type: `-` = regular file, `d` = directory|
|Positions 2-4|Owner permissions|
|Positions 5-7|Group permissions|
|Positions 8-10|Everyone else (others)|

**Permission Letters**

|Letter|Meaning|Value|
|---|---|---|
|`r`|read|4|
|`w`|write|2|
|`x`|execute|1|
|`-`|no permission|0|

**Numeric System — add the values together**

```
7 = 4+2+1 = rwx (full access)
6 = 4+2   = rw- (read and write)
5 = 4+1   = r-x (read and execute)
4 = 4     = r-- (read only)
0 = 0     = --- (no access)
```

**Common Permission Combinations**

|chmod|Owner|Group|Others|Use case|
|---|---|---|---|---|
|755|rwx|r-x|r-x|Shared tools like python3|
|600|rw-|---|---|SSH keys, private files|
|644|rw-|r--|r--|Regular readable files|
|777|rwx|rwx|rwx|Dangerous — avoid always|

**Owner and Group**

- Every file has an **owner** (one person) and a **group** (a collection of users)
- Groups allow controlled shared access — members get group permissions, everyone else gets others permissions
- Example: security team all in `staff` group can read team files, but outsiders cannot

`gtfobins.github.io` — documents every Linux binary that can be abused for privilege escalation.