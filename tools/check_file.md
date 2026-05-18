```bash
#Task: Write a function called `check_file` that takes a filename as its argument and does the following:

#1. If no argument was given, prints `"Usage: check_file <filename>"` and returns 1.
#1. If the file exists, prints `"<filename> exists."` and then prints the number of lines in that file.
#1. If the file does not exist, prints `"<filename> does not exist."` and returns 1.

#After defining the function, call it with `check_file "$1"` so the script can be run as `./script.sh somefile`.

check_file() {
	if [ -z "$1" ]; then
		echo "Usage: check_file <filename>"
		return 1
	fi
	if [ -f "$1" ]; then
		echo "$1 exists"
		wc -l < "$1"
	else
		echo "$1 does not exist"
		return 1
	fi
}
check_file "$1"

--------------------------------------------------

check_file() {
	if [ -z "$1" ]; then
		echo "Usage: check_file <filename>"
		return 1
	fi
	if [ -f "$1" ]; then
		echo "$1 exists"
		wc -l < "$1"
	else
		echo "$1 does not exist"
		return 1
	fi
}
if [ $# -eq 0 ]; then
	echo "Usage: check_files <file1> [file2] ..."
	exit 1
fi
for file in "$@"; do
	check_file "$file"
done
```