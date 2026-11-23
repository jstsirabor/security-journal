#!/bin/bash

target_file="/etc/fake_file.txt"
backup_dir="/tmp"

if [ -f "$target_file" ]; then
	echo "File found. Backing up to $backup_dir"
	cp "$target_file" "$backup_dir"
	echo "THe error status for the cp is: $?"
else
	echo "Error: File not found"
fi
