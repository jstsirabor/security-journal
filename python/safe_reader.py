filename = "/etc/fake_file.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"{filename} file opened successfully")
        print(content)
except FileNotFoundError:
    print(f"Error: The {filename} file does not exist")
except PermissionError:
    print(f"Error: You do not have the permission to read the {filename} file.")
