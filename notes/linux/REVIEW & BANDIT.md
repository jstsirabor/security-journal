### Git – Week 1 Push

|Command|Action|
|---|---|
|`git init`|Initialize a git repository|
|`git add .`|Stage all files|
|`git commit -m "message"`|Commit staged changes|
|`git branch -M main`|Rename branch to main|
|`git remote add origin <url>`|Link to GitHub repository|
|`git push -u origin main`|Push commits to GitHub|

### SSH – Connecting to Remote Servers

|Command|Action|
|---|---|
|`ssh user@host -p port`|Connect to a remote server via SSH|
|`exit`|Close the SSH connection|

### Bandit Level 0–5 Commands Used

| Level | Command(s)                            | What It Taught                      |
| ----- | ------------------------------------- | ----------------------------------- |
| 0 → 1 | `cat readme`                          | Reading files                       |
| 1 → 2 | `cat ./-`                             | Handling dashed filenames           |
| 2 → 3 | `cat "spaces in this filename"`       | Handling filenames with spaces      |
| 3 → 4 | `ls -a`, `cat .hidden`                | Hidden files                        |
| 4 → 5 | `file ./*`, `cat` human-readable ones | Identifying file types              |
| 5 → 6 | `find . -size 1033c ! -executable`    | File size and permissions filtering |

