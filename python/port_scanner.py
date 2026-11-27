def parse_port(port):
    try:
        port = int(port)
        if 1 <= port <= 65635:
            return port
        else:
            return "Port out of range"
    except ValueError:
        return "Invalid port format"

print(parse_port("80"))
print(parse_port("hello"))
print(parse_port("70000"))