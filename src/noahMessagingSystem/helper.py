def in_users(users, user, password):
    for u in users:
        if u['user'] == user and u['password'] == password:
            return True
    return False