def scan_target(ip_address, port=80):
    return f"Scanning {ip_address} on port {port}..."

scan_result = scan_target("192.168.1.1", 22)
print(scan_result)