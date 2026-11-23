host = {
    "name": "webserver",
    "ip": "192.168.1.50",
    "services": ["http", "https", "ssh"],
    "admin":{"username": "root", "privileged": True}
}
print(host["services"][1])
print(host["admin"]["username"])
print(host["ip"])