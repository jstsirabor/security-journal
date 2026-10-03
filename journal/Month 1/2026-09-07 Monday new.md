## Date: 2026-09-07

### What I tried
-

### What broke
-

### What I learned
- Using `.` is not redundant. It forces to be explicit when calling files or folders in the current directory, `./`.
- `\t` is use to add tab in python
- `\n` is used to move to new line in python
- `lstrip()` and `rstrip()` are used to remove white spaces from a string left and right respectively. They are mostly used to clean up user input before being stored in a program. `strip()` removes both  at once.
- `removeprefix("prefix")` is used to remove prefix from a string and `removesuffix` to remove suffix
- Syntax error occurs when python doesn't recognize a part of the program as a valid python code.
- The hash mark (#) represents comments in python
- A return statement sends the value back out of the function to wheover called it, so the result can be used elsewhere in the program.
- Scope is the idea that a variable created in a function can be used only in that function. It is a deliberate safety measure
- `dig example.com` helps query dns and returns the raw output - the actual ip address and the duration for which it is valid
- Syn flood involves client sending a lot of SYN requestion and dropping the connection so ACK is never received by the server. This would exhaust the servers capacity to handle legitimate connection attempts.

### Commands/code worth remembering
```code
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
```

### Questions for later
-