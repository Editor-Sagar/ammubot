import random

NEWS = [
    "Bengaluru traffic jam today again 😭",
    "Heavy rain expected in Karnataka 🌧️",
    "Tech layoffs news trending again 📉",
    "New metro route announced 🚇",
    "Karnataka government announces new scheme 💡"
]

def get_trending_news():
    return random.choice(NEWS)
