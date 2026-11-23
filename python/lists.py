open_ports = [22, 80, 443]
print(open_ports)
open_ports.append(8080)
open_ports.remove(80)
print(len(open_ports))
print(open_ports)
print(open_ports[0])
print(open_ports[-1])