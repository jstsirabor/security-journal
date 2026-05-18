```bash
#The task was to write a script called `scan_logs.sh` that:
#1. Takes a directory as an argument.
#2. If no argument, prints usage and exits.
#3. If not a directory, prints error and exits.
#4. Loops over every `.log` file in that directory.
#5. For each file, prints a header `=== filename ===` and counts how many lines contain `Failed`.
#6. If no `.log` files exist, says so.
#7. After the loop, prints `Scan complete.`
   
#!/bin/bash

if [ -z "$1" ]; then
   echo "Usage: scan_logs.sh <directory>"
   exit 1
fi
if [ -d "$1" ]; then
   found=0
   for file in "$1"/*.log; do
        if [ -f "$file" ]; then
            echo "=== $file ==="
            grep -i -c "failed" "$file"
            found=1
        fi
   done
   if [ $found -eq 0 ]; then
        echo "No log files found."
   fi
else
   echo "The directory does not exist"
   exit 1
fi
echo "Scan complete."
```