with open("access.log", "r") as file:
    for line in file:
        print(line.strip())