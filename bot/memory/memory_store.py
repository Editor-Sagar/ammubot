import json, os

FILE = "data/users.json"

def load():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def get_user(uid):
    data = load()
    if str(uid) not in data:
        data[str(uid)] = {}
        save(data)
    return data[str(uid)]
