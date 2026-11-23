def validate_port(port):
    if port > 65535:
        raise ValueError("Port cannot be greater than 65535")
    else:
        return "Valid port"


print(validate_port(80))
try:
    print(validate_port(70000))
except ValueError as e:
    print(e)
finally:
    print("Validation process finished")