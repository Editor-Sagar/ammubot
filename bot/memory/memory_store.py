import json
import os

FILE = "data/users.json"

def load_users():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save_users(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user(user_id):
    data = load_users()
    if str(user_id) not in data:
        data[str(user_id)] = {"mood": "neutral"}
        save_users(data)
    return data[str(user_id)]
