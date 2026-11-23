user_input = "22"
try:
    int_convert = int(user_input)
    print(f"Successfully converted {user_input} to an integer: {int_convert}")
except ValueError:
    print(f"Error: {user_input} is not a valid number!")