import os
filename = "access.log"

if os.path.exists(filename):
    print("File found. Ready to parse")
else:
    print("Error: File not found")