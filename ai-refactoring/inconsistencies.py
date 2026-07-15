def get_user(user_id):
    return {"id": user_id, "name": "unknown", "active": True}


def update_user(user, new_name):
    user["name"] = new_name
    return user


def delete_user(users, user_id):
    for index in range(len(users)):
        if users[index]["id"] == user_id:
            del users[index]
            return True
    return False
