log_line = "Connection to port 22"
log_line_split = log_line.split()
port_number = log_line_split[-1]
int_port_num = int(port_number)
next_port = int_port_num + 1
print(f"The next port is {next_port}")
