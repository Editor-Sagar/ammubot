BAD_WORDS = ["badword1", "badword2"]

def contains_abuse(text):
    return any(w in text.lower() for w in BAD_WORDS)
