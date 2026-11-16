

**The Challenge:** The password is hidden inside a file that has been compressed and archived multiple times.

**The Golden Rule:**  
Every time you unpack a layer, **immediately run `file <filename>`** on the result to see what the next layer is.

**Step 1: The Setup**

- Your home directory is read-only, so you **must** create a directory in `/tmp` and work there.
    
- You tried `mv`, which failed with `Permission denied`. You correctly switched to `cp`.
    
    bash
    
    mkdir /tmp/testdir
    cp ~/data.txt /tmp/testdir/
    cd /tmp/testdir
    

**Step 2: Reverse the Hex Dump**

- The initial `data.txt` is a hex dump. You must reverse it into binary.
    
    bash
    
    xxd -r data.txt > data.bin
    

_(Note: If you accidentally run this before copying the file, you get an empty `data.bin`. If so, just `rm data.bin` and try again)._

**Step 3: The Decompression Loop**

- Run `file data.bin` to see the format. Then use the corresponding tool.
    
- **If gzip:** `gzip` refuses to run if the file doesn't end in `.gz`. So, rename it, then decompress:
    
    bash
    
    mv data.bin data.gz
    gzip -d data.gz
    
- **If bzip2:** Same rule. Rename to `.bz2`, then decompress:
    
    bash
    
    mv data data.bz2
    bzip2 -d data.bz2
    
- **If tar:** A tar archive is a box containing files. Extract it:
    
    bash
    
    tar -xf data.tar
    

**Step 4: The Finish Line**

- Keep running `file <newfile>` and using the matching tool until `file` says **ASCII text**.
    
- Finally, read the text:
    
    bash
    
    cat data8
    

**Top 1% Lessons from this Level:**

1. **`cp` vs `mv`:** When a directory is read-only (like the Bandit home directories), you can't move files out, but you can copy them.
    
2. **File Extensions Matter:** Tools like `gzip` and `bzip2` care deeply about file extensions. If a tool complains about an "unknown suffix," just `mv` the file to the correct extension.
    
3. **`file` is your best friend:** Never guess what a file is. Look at the magic bytes.