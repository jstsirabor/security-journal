### What is `sed`?

`sed` stands for **stream editor**. It reads text **line by line**, applies transformations, and outputs the result.

Think of it as `awk`'s sibling:

- `awk` = extracting and reporting.
    
- `sed` = editing (substitution, deletion, insertion).
    

---

### Core Syntax

bash

sed 'command' file

- `command` = what to do (substitute, delete, print, etc.).
    
- `file` = the input file (optional; can read from a pipe or stdin).
    

---

### Substitution — `s/old/new/`

|Command|What it does|
|---|---|
|`sed 's/old/new/' file`|Replace the **first** occurrence of `old` on **each line**|
|`sed 's/old/new/g' file`|Replace **every** occurrence of `old` on **each line**|

**Key facts:**

- `sed` processes line by line. Default is one replacement per line.
    
- `g` = global (all occurrences per line, not per file).
    

**Examples:**

bash

echo "hello world hello" > sed_test.txt
sed 's/hello/HI/' sed_test.txt       # HI world hello
sed 's/hello/HI/g' sed_test.txt      # HI world HI
echo "hello world" | sed 's/world/there/'    # hello there

---

### Deletion — `d`

|Command|What it does|
|---|---|
|`sed '/pattern/d' file`|Delete lines matching `pattern`|
|`sed '3d' file`|Delete line 3|
|`sed '2,5d' file`|Delete lines 2 through 5|

**Important:** `sed` doesn't modify the original file unless you use `-i`. It prints the filtered output.

**Examples:**

bash

sed '/Failed/d' awk_exercise.log      # shows only lines without "Failed"
sed '/Accepted/d' awk_exercise.log    # shows only lines without "Accepted"
sed '1d' awk_exercise.log             # shows all lines except line 1

---

### Multiple Commands — `-e`

Chain multiple commands together:

bash

sed -e 's/old/new/' -e '/pattern/d' file

Each `-e` adds one command. They run **in order** on each line.

**Equivalent with semicolons:**

bash

sed 's/old/new/; /pattern/d' file

**Example:**

bash

sed -e 's/from/IP:/' -e '/Accepted/d' awk_exercise.log

- First: replace `from` with `IP:` on every line.
    
- Then: delete lines containing `Accepted`.
    

**Result:** Only failed lines remain, with `from` changed to `IP:`.

---

### In-Place Editing — `-i`

|Command|What it does|
|---|---|
|`sed 's/a/b/' file`|Prints changes to terminal. File is **unchanged**.|
|`sed -i 's/a/b/' file`|**Modifies the file directly.** Irreversible.|

**Warning:** `-i` overwrites the original file. There is no undo.

**Safe practice:** Always test without `-i` first, verify the output, then add `-i`.

**Example:**

bash

echo "hello world" > inplace_test.txt
sed 's/hello/HI/' inplace_test.txt      # output: HI world, file unchanged
sed -i 's/hello/HI/' inplace_test.txt   # file now contains HI world

---

### Capture Groups — `\(...\)` and `\1`, `\2`

Capture groups let you **grab a part of the line, remember it, and reuse it** in the replacement.

**Basic syntax:**

bash

sed 's/\(capture\)/replacement \1/' file

- `\(...\)` — captures what's inside. This becomes group 1.
    
- `\1` — refers to the first captured group (puts it back).
    
- `\2` — refers to the second captured group.
    

---

#### Simple example: Wrapping text

bash

echo "hello world" | sed 's/\(hello\)/[\1]/'

Output: `[hello] world`

- `\(hello\)` — find `hello` and capture it as group 1.
    
- `[\1]` — replace it with `[` + captured text + `]`.
    

---

#### Two groups: Swapping words

bash

echo "John Smith" | sed 's/\(John\) \(Smith\)/\2 \1/'

Output: `Smith John`

- `\(John\)` — capture group 1.
    
- `\(Smith\)` — capture group 2.
    
- `\2 \1` — output group 2, space, group 1.
    

---

#### General version (any names)

bash

echo "Alice Johnson" | sed 's/\([A-Za-z]*\) \([A-Za-z]*\)/\2 \1/'

Output: `Johnson Alice`

- `[A-Za-z]*` — any sequence of letters (uppercase or lowercase).
    
- Works for any two-word name.
    

---

#### Extracting an IP from a log line

bash

echo "Failed password for admin from 192.168.1.100 port 22" | sed 's/.*from \([0-9.]*\) port.*/\1/'

Output: `192.168.1.100`

**Breakdown:**

|Part|What it matches|
|---|---|
|`.*from`|Everything from the **start of the line** up to and including `from`|
|`\([0-9.]*\)`|**Captures** the IP — any sequence of digits and dots|
|`port.*`|The word `port` and everything after it|
|`\1`|Replace the whole match with just the captured IP|

**Correction to note:** `.*from` matches from the **start** of the line to `from`. Not "from `from` to the end." `.*` means "any characters (greedy)" and starts from the beginning.

---

### `sed` vs `awk` for IP extraction

| Task                         | `sed` approach                                      | `awk` approach                                           |
| ---------------------------- | --------------------------------------------------- | -------------------------------------------------------- |
| Extract IP                   | `sed 's/.*from \([0-9.]*\) port.*/\1/'`             | `awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}'` |
| When to use                  | When the line has a **fixed pattern** around the IP | When the field number **may vary**                       |
| Handles "invalid user test"? | Yes, because it matches `from ... port` pattern     | Yes, because it finds the word `from`                    |

**Both work for log analysis.** `sed` is better when the surrounding text is predictable. `awk` is better when you need to work with variable field positions or do calculations.

---

### Key Corrections from This Session

|What you said|Correction|
|---|---|
|_"`sed 's/hello/HI/'` replaces first occurrence in file"_|It replaces the first occurrence **on each line**, not in the file.|
|_"`g` means all round the file"_|`g` means all occurrences **on each line**. Still line by line.|
|_"`.*from` matches from `from` to the end"_|`.*from` matches from the **start of the line** up to and including `from`.|

---

### Full `sed` Summary Table

| Command                                    | Purpose                           |
| ------------------------------------------ | --------------------------------- |
| `sed 's/old/new/' file`                    | Replace first occurrence per line |
| `sed 's/old/new/g' file`                   | Replace all occurrences per line  |
| `sed '/pattern/d' file`                    | Delete lines matching pattern     |
| `sed '3d' file`                            | Delete line 3                     |
| `sed '2,5d' file`                          | Delete lines 2–5                  |
| `sed -e 'cmd1' -e 'cmd2' file`             | Multiple commands                 |
| `sed 'cmd1; cmd2' file`                    | Multiple commands (semicolon)     |
| `sed -i 's/a/b/' file`                     | Edit file in place                |
| `sed 's/\(capture\)/replacement \1/' file` | Capture and reuse                 |
| `sed 's/.*from \([0-9.]*\) port.*/\1/'`    | Extract IP from log line          |