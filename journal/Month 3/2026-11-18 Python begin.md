## Date: 2026-11-17

### What I tried
- When you read data from a log file, a web form, or a config file, Python reads it as a **String** (text), even if it's just a number. If you try to do math on it, it will break.
- Type `exit()` to leave the Python shell and go back to your regular terminal.
- The scripts I'm writing would ask questions like Is port open? The answer would usually be stored as True or False
- If a log file is missing an IP address field, Python would assign it as None

### What broke
-

### What I learned
- Virtual environment (.venv) helps keep python projects isolated so they don't break the system
- Python is strongly typed. It doesn't guess. This strictness prevents huge classes of security vulnerabilities (like type confusion attacks) later.
- F-strings let you embed variables directly into a string. The syntax is a quote, preceded by an `f`. Inside the string, you use curly braces `{}` to insert the variable.
	- print(f"User {name} is connecting to port {port}.")
- F-strings are the backbone of security reporting.
- Boolean is exactly two possible values which are True or False.
- `None` is a special value that means "nothing" or "empty."
- Python is **dynamically typed and strongly typed**. Variables do not have fixed declared types, but Python does not silently mix incompatible values.
- A virtual environment isolates project-installed packages; it helps you avoid altering the system Python’s package set, but it does not make the system Python impossible to affect.
- Rename `math.py` to something like `ports.py`. `math` is a Python standard-library module, and your file could shadow it later.
- `None` means “no value / absence of a value,” not necessarily an empty value.
- In a security tool, `False` should often mean “this check did not detect the condition,” not “the system is definitively safe.”

### Commands/code worth remembering
```code

```

### Questions for later
-