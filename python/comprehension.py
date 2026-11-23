ports = [22, 80, 443, 8080, 21, 3306]
filtered_ports = [port for port in ports if port > 100]
print(filtered_ports)