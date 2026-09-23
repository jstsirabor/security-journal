## Date: 2026-09-23

### What I tried
- `grep "Failed password" /var/log/auth.log | cut -d " " -f 10 | sort | uniq -c | sort -nr`. Each `|` connects stdout to stdin: 1. `grep` outputs matching lines, 2. `cut` reads those lines, extracts field 10, 3. `sort` reads the IPs, sorts them, 4.`uniq -c` counts adjacent duplicates, 5. `sort -nr` sorts by count descending.
- Don't use `grep -v` to find "success." Use `grep` to match the specific string you want (`Accepted`). `-v` is for excluding noise, not for finding a specific category.
- `uniq -c` only counts **adjacent** duplicates. Without sorting first, identical entries that aren't next to each other get counted separately. That's why you see `admin` three times and `root` twice instead of one combined count.
- 
### What broke
-

### What I learned
- Every Linux process has three default data streams: **stdin**(0) -> Standard input, **stdout**(1) -> Standard output, **stderr**(2) -> Standard error
- Pipe connects the stdout of the left command to the stdin of the right command. `command1 | command2`
- The pipe only connects stdout, not stderr. If `command1` writes an error, it goes to the terminal, not through the pipe.
- To send stderr into the pipe as well, you use `2>&1`: `command1 2>&1 | command2`. This says: "Send stderr (2) to the same place as stdout (1), then pipe both." For instance, `find / -name "*.conf" 2>/dev/null | wc -l` -> 2>/dev/null sends error to the void (discards them)
- 

### Commands/code worth remembering
```code
1. grep ... | cut ... | sort | uniq -c | sort -nr

```

### Questions for later
-