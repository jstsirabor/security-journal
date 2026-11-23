#!/bin/bash
read -p "Enter username: " user

if [ "$user" = "root" ]; then
	echo "Warning: You are running as root"
else
	echo "You are a normal user: $user"
fi
