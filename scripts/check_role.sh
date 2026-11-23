#!/bin/bash

read -p "Enter username: " user

if [ "$user" = "root" ]; then
	echo "Superuser: Full control"
elif [ "$user" = "admin" ]; then
	echo "Admin: Elevated control"
else
	echo "User: Limited control"
fi
