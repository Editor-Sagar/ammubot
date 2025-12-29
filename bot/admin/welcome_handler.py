import random

WELCOME_MESSAGES = [
    "Hey {name} 👋 Welcome to the group!",
    "Namaskara {name} 😊 Welcome!",
    "Glad you joined us, {name} 🎉",
    "Heyyy {name} 😄 Welcome aboard!"
]

def welcome_user(name):
    return random.choice(WELCOME_MESSAGES).format(name=name)
