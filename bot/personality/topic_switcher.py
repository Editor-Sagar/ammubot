import random

def switch_topic():
    topics = [
        "By the way, what are you doing now?",
        "So… how was your day?",
        "Tell me something interesting 😄",
        "What’s on your mind?"
    ]
    return random.choice(topics)
