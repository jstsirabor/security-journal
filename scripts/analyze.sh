#!/bin/bash

log_file=${1}

if [ ! -f "$log_file" ]; then
	echo "This file does not exist"
	exit 1
else
	echo "Total lines: $(wc -l < "$log_file")"
	echo "Failed logins: $(grep -ci 'Failed' "$log_file")"
	echo "Accepted logins: $(grep -ci 'Accepted' "$log_file")"
	echo "--- First 5 lines ---"
	echo 
	echo "$(head -n 5 "$log_file")"
fi
