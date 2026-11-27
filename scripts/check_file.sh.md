```bash
#!/bin/bash

filename="$1"

if [ -z "$filename" ]; then
    echo "Error: No file provided"
    exit 1
elif [ ! -f "$filename" ]; then
    echo "Error: File does not exist"
    exit 1
else
    echo "File found. Counting lines..."
    wc -l < "$filename"
fi
```