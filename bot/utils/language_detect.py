import re

# Word banks for mixed languages
KANNADA_WORDS = [
    "macha", "machaa", "maga", "maga", "yaake", "beku", "illa",
    "sari", "namma", "hog", "hogbeka", "thumba", "andre"
]

HINDI_WORDS = [
    "kya", "kyu", "hai", "nahi", "haan", "mera", "tera",
    "acha", "theek", "kar", "raha", "bhai"
]

TELUGU_WORDS = [
    "enti", "emi", "ledu", "undhi", "bagundi",
    "ra", "raaa", "nenu", "meeru", "cheppu"
]

TAMIL_WORDS = [
    "enna", "irukku", "illa", "romba", "seri",
    "poda", "sapadu", "enna da", "epdi"
]

def detect_language(text: str) -> str:
    text = text.lower()
    words = re.findall(r"[a-zA-Z]+", text)

    score = {
        "kanglish": 0,
        "hinglish": 0,
        "teluglish": 0,
        "tamilish": 0
    }

    for word in words:
        if word in KANNADA_WORDS:
            score["kanglish"] += 1
        if word in HINDI_WORDS:
            score["hinglish"] += 1
        if word in TELUGU_WORDS:
            score["teluglish"] += 1
        if word in TAMIL_WORDS:
            score["tamilish"] += 1

    # Default to English if nothing matches
    if max(score.values()) == 0:
        return "english"

    return max(score, key=score.get)
