### Basic Structure

bash

awk 'pattern { action }' file

- `pattern` — optional. If omitted, action runs on every line.
    
- `action` — what to do (usually `print`).
    
- `file` — the file to process.
    

---

### Fields

|Field|Meaning|
|---|---|
|`$0`|Entire line|
|`$1`|First field|
|`$2`|Second field|
|...|...|
|`$NF`|Last field|
|`$(NF-1)`|Second-to-last field|
|`$(NF-3)`|Fourth-to-last field|

**Default separator:** whitespace (spaces or tabs).

---

### Built-in Variables

|Variable|Meaning|
|---|---|
|`NR`|Current line number (record number)|
|`NF`|Number of fields in the current line|
|`$0`|The entire current line|
|`FS`|Input field separator (default: whitespace)|
|`OFS`|Output field separator (default: space)|

---

### Custom Delimiter

bash

awk -F: '{print $1}' /etc/passwd

`-F:` sets the input field separator to colon.

---

### Pattern Matching

bash

awk '/Failed/ {print $10}' file

Only processes lines containing "Failed".

**Case-insensitive:**

bash

awk 'tolower($0) ~ /failed/ {print $10}' file

Note: `tolower($0)` converts to lowercase, so the pattern must also be lowercase.

---

### Conditions

bash

awk '$3 > 100 {print $1}' numbers.txt

Prints field 1 for lines where field 3 is greater than 100.

bash

awk '/Failed/ && $10 ~ /^192\./ {print $10}' file

Prints IPs starting with `192.` on lines containing "Failed".

---

### Calculations

bash

awk '{sum += $2} END {print sum}' numbers.txt

Sums field 2 across all lines.

bash

awk 'END {print NR}' file

Counts lines.

bash

awk '{sum += $2} END {print sum/NR}' file

Average of field 2.

---

### Field Extraction by Content

bash

awk '/Failed/ {for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' file

Finds the field equal to `from` and prints the next field (the IP). Works even when extra words shift field numbers.

**Username extraction (same technique):**

bash

awk '/Failed/ {for(i=1;i<=NF;i++) if($i=="for") print $(i+1)}' file

---

### Output Formatting

**Using `printf`:**

bash

awk '/Failed/ {printf "IP: %s\n", $10}' file

- `%s` — string placeholder.
    
- `\n` — newline.
    

**Using `OFS`:**

bash

awk 'BEGIN {OFS=":"} {print $1, $2}' file

Changes output separator from space to colon.

---

### Full Pipeline with `awk`

bash

awk '/Failed/ {for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' auth.log | sort | uniq -c | sort -nr

Replaces `grep | cut | sort | uniq -c | sort -nr` with a more robust extraction.