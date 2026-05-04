**grep — Finding Patterns Inside Files**

|Command|What it does|
|---|---|
|`grep 'pattern' file`|Lines containing pattern|
|`grep -i 'pattern' file`|Case insensitive|
|`grep -n 'pattern' file`|Include line numbers|
|`grep -v 'pattern' file`|Lines NOT containing pattern|
|`grep -c 'pattern' file`|Count matching lines|
|`grep -r 'pattern' /dir/`|Search recursively through directory|

**find — Locating Files by Properties**

| Command                        | What it does             |
| ------------------------------ | ------------------------ |
| `find /dir -name '*.txt'`      | Find by filename pattern |
| `find / -type f -name '*.log'` | Files only               |
| `find / -perm -4000`           | All SUID files           |
| `find / -writable`             | All writable files       |

**2>/dev/null** — redirects error messages to `/dev/null` (Linux black hole). Keeps output clean by hiding permission denied errors.

**Pipes `|` — Chaining Commands**

Sends output of one command as input to the next. Each tool does one thing — pipes connect them into powerful pipelines.

bash

```bash
grep 'Failed' auth.log | awk '{print $11}' | sort | uniq -c
```

**awk — Text Processing**

Splits each line into numbered fields by whitespace:

```
Jan  1  10:00:01  server  sshd:  Failed  password  for  root  from  10.0.0.1
$1   $2    $3       $4     $5      $6       $7      $8   $9    $10     $11
```

|Command|What it does|
|---|---|
|`awk '{print $1}'`|Print first field|
|`awk '{print $1, $3}'`|Print multiple fields|
|`awk '{print $NF}'`|Print last field|
|`awk '$6 == "Failed" {print $11}'`|Conditional printing|

**sort and uniq**

|Command|What it does|
|---|---|
|`sort`|Arranges output alphabetically/numerically|
|`uniq`|Removes consecutive duplicates (always sort first)|
|`uniq -c`|Counts occurrences of each unique line|