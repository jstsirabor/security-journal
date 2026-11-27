### The Types of Errors (Top 1% Guide)

You asked for all the types of errors. Here is the complete taxonomy of errors you will face as a Python and Bash developer, categorized exactly how an engineer thinks about them.

#### Category 1: Syntax Errors (The code can't even run)

These happen when you break the grammar of the language. The interpreter stops immediately.

- **Bash:** Missing `fi`, spaces inside `[condition]`, using `else if` instead of `elif`.
    
- **Python:** Missing colon `:` at the end of a `def` or `if`, missing quotes around a string, mismatched parentheses.
    
- _Rule:_ The code will not execute. The interpreter highlights the line.
    

#### Category 2: Logic Errors (The code runs, but does the wrong thing)

This is the most dangerous type because the program doesn't crash. It silently gives you the wrong answer.

- **Bash:** Writing `[ -z "$1" ]` when you meant `[ ! -f "$1" ]`. (The script runs, but it checks the wrong thing).
    
- **Python:** Using `=` (assignment) instead of `==` (comparison) in an `if` statement. Or using `//` (integer division) when you meant `/` (float division) and losing a decimal point.
    
- _Rule:_ No error message is generated. You only find it by testing or reviewing your code.
    

#### Category 3: Runtime Errors (Exceptions in Python)

These happen _while_ the code is running. The syntax is perfect, but reality breaks the code.

- **`FileNotFoundError`:** Trying to open a file that isn't there.
    
- **`PermissionError`:** Trying to read `/etc/shadow` as a normal user.
    
- **`ValueError`:** Trying `int("twenty-two")`.
    
- **`KeyError`:** Trying `dict["missing_key"]`.
    
- **`IndexError`:** Trying `list[5]` when the list only has 3 items.
    
- **`TypeError`:** Trying `"5" + 5`.
    
- _Rule:_ The script crashes with a Traceback. You handle these with `try/except`.
    

#### Category 4: Semantic Errors (The "Empty File" Trap)

These look like runtime errors, but are actually caused by bad input or state.

- **`JSONDecodeError`:** You tried to parse an empty file as JSON. (The error you just got).
    
- **`AttributeError`:** You tried to call `.get()` on a string instead of a dictionary.
    
- _Rule:_ The code is fine; the data it was fed was wrong.
    

#### Category 5: Process/System Errors (Linux level)

These happen at the OS level.

- **`Permission denied`:** Running `./script.sh` without `chmod +x`.
    
- **`Command not found`:** Typing `python` instead of `python3`.
    
- **`No such file or directory`:** Trying to `cd` into a folder that doesn't exist.
    
- **`Killed` (OOM):** Your script used too much RAM and the Linux kernel killed it.