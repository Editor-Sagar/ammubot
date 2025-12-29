import random

# Simple AI-style responses (lightweight & fast)
RESPONSES = [
    "Hey 😄 what's up?",
    "Haha 😆 that's interesting!",
    "Tell me more 👀",
    "Hmm 🤔 sounds interesting",
    "Ohh nice 😌",
    "Haha good one 😂",
    "I'm listening 👂",
    "That's cool 😎",
    "Wow, really? 😮",
    "Go on… 😊"
]

def ai_reply(text: str) -> str:
    """
    Returns a friendly AI-style response.
    """
    return random.choice(RESPONSES)
