def detect_language(text):
    text = text.lower()

    if any(w in text for w in ["namma", "sari", "illa"]):
        return "kannada"
    if any(w in text for w in ["kya", "hai", "nahi"]):
        return "hindi"
    if any(w in text for w in ["enna", "irukku"]):
        return "tamil"
    return "english"
