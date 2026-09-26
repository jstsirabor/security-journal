
You've used `history` before (`history -c`, `history -w`). Now we go deeper — these shortcuts make you dramatically faster.

---

### `!!` — Repeat the last command

bash

!!

This runs the exact last command you typed. Useful when you forgot to prefix a command with `sudo`:

bash

apt install nginx        # fails, needs sudo
sudo !!                  # runs "sudo apt install nginx"

---

### `!$` — Last argument of the last command

bash

!$

This expands to the **last argument** of your previous command.

**Example:**

bash

mkdir /tmp/testdir
cd !$                     # cd /tmp/testdir

---

### `!n` — Run command number `n`

bash

!42

Runs the command with history number 42 (from `history` output).

---

### `!string` — Run the most recent command starting with `string`

bash

!grep

Runs the most recent command that started with `grep`.

---

### `Ctrl+R` — Interactive reverse search

This is the most useful one. Press **Ctrl+R** in your terminal, then start typing. It searches your command history and shows matches as you type. Press **Ctrl+R** again to cycle through older matches. Press **Enter** to run the matched command, or **Ctrl+C** to cancel.