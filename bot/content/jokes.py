import random

JOKES = [
    "Why did the phone break up with WiFi? Too many disconnects 😂",
    "I tried to be normal once... worst 5 minutes of my life 😆",
    "My brain has too many tabs open 😵‍💫",
    "Why don’t programmers like nature? Too many bugs 🐞",
    "I told my boss I need a raise… he said ‘stand up’ 😭"
]

def get_joke():
    return random.choice(JOKES)
