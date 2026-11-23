#!/bin/bash
ls /etc/passwd
echo "Exit code: $?"

ls /nonexistent
echo "Exit code: $?"
