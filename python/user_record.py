user_record = {
    "username": "admin",
    "uid": 0,
    "ssh_keys": ["key1.pem", "key2.pem"],
    "permissions": {"read": True, "write": True, "execute": True}
}
print(user_record["ssh_keys"][1])
print(user_record["permissions"]["write"])
print(user_record)