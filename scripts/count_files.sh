#!/bin/bash

target_dir="/etc"
counter=0

for file in "$target_dir"/*; do
	echo "Checking: $file"
	counter=$((counter + 1))
done

echo "Total files checked: $counter"
