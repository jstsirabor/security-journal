```bash
#!/bin/bash
#This script takes a log file to perform some action

FILE_NAME=$1
if [ -z "$FILE_NAME" ]; then
        echo "No file given"
        exit 1
fi

if [ -f "$FILE_NAME" ]; then
        TOTAL_LINES=$(wc -l "$FILE_NAME" | awk '{print $1}')
        FAILED_LINES=$(grep -c -i "failed" "$FILE_NAME")
        ACCEPTED_LINES=$(grep -c -i "accepted" "$FILE_NAME")

        echo "The total number of lines is $TOTAL_LINES"
        echo "The number of failed lines is $FAILED_LINES"
        echo "The number of accepted lines is $ACCEPTED_LINES"
        head -n 5 "$FILE_NAME"
else
        echo "This file does not exist."
fi
```


```bash
#!/bin/bash
FILE=$1

if [ -z "$FILE" ]; then
     echo "No file is given"
     exit 1
fi
if [[ -f "$FILE" && "$FILE"=="auth.log" ]]; then
     TOTAL=$(wc -l < "$FILE")
     FAILED=$(grep -ci "failed" "$FILE")
     SUCCESS=$(grep -ci "accepted" "$FILE" | wc -l)

     echo "Total attempts: $TOTAL"
     echo "Failed attempts: $FAILED"
     echo "Successful attempts: $SUCCESS"
     head -n 5 "$FILE"
else
     echo "Error: file not found"
fi
```