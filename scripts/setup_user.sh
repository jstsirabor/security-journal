#!/bin/bash

read -p "Enter username:" username
home_dir=${1:-/home}

echo "Setting up user $username in directory $home_dir"
