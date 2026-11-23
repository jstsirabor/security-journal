def check_login(username, failed_attempts):
    if failed_attempts >= 5:
        return f"ALERT: {username} has {failed_attempts} failed attempts"
    else:
        return f"OK: {username} is within normal limits"



admin = check_login("admin", 6)
print(admin)
guest = check_login("guest", 2)
print(guest)