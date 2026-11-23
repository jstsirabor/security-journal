#!/bin/bash
read -p "What is the file name? ${1}" arg1
read -p "What word are you looking for? ${2}" arg2

grep arg2 arg1
echo "The exit status for grep is $?"
