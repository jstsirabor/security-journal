#!/bin/bash

read -p "What is your name? " name
read -p "what is your age? " age

echo "Hello $name, you will be $((age + 1)) next year"
