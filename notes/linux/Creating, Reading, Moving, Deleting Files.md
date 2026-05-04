**Creating Files**

```bash
touch myfile.txt      # creates empty file (size 0)
mkdir myfolder        # creates a directory
```

**Reading Files**

```bash
cat filename          # prints entire file at once
less filename         # page by page (space=next, q=quit)
head filename         # first 10 lines
tail filename         # last 10 lines
tail -f filename      # live view — new lines appear in real time
```

`tail -f` is critical for security work — run it on `/var/log/auth.log` to watch attacks happen in real time.

**Writing to Files**

```bash
echo 'text' > file    # OVERWRITES entire file
echo 'text' >> file   # APPENDS to end, preserves content
```

Security tools always use `>>` for logs — never `>`. Using `>` destroys previous entries.

**Moving, Copying, Deleting**

```bash
cp file1 file2        # duplicate — two files exist after
mv file1 newname      # rename/move — one file exists after
rm file               # delete permanently — no recycle bin
rm -rf folder         # delete folder and ALL contents — no warning, no undo
```

`rm -rf` is one of the most dangerous commands in Linux. Always double-check your path before running it.
