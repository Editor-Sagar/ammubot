import random

def human_reply(text):
    replies = [
        "Hey 😄",
        "Tell me more!",
        "Haha nice 😄",
        "I'm listening 👂",
        "That’s interesting!"
    ]
    return random.choice(replies)
