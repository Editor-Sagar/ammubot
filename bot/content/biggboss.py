import random

BIGGBOSS_LINES = [
    "Bigg Boss house full drama today 😮",
    "Fight again in Bigg Boss house 🔥",
    "Audience shocked by today's eviction 😱",
    "Task today was full of drama 😅",
    "Contestants planning secret strategies 😏"
]

def get_biggboss_update():
    return random.choice(BIGGBOSS_LINES)
