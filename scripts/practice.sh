#!/bin/bash

echo "===Script Info ==="
echo "Script name: $0"
echo "First arg: ${1:-none}"
echo "Second arg: ${2:-none}"
echo "All args: $@"
echo "Arg count: $#"

echo
echo "=== Variables ==="
name="Darkhand"
echo "Name: $name"
echo "Home: $HOME"
echo "User: $USER"

echo
echo "=== User Input ==="
read -p "What's your favorite tool? " tool
echo "You chose: $tool"

echo
echo "=== Exit Code Test ==="
ls /etc/passwd > /dev/null
echo "ls /etc/passwd exit code: $?"

ls /nonexistent 2>/dev/null
echo "ls /nonexistent exit code: $?"
