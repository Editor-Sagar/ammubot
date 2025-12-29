def detect_mood(text):
    text = text.lower()

    if any(w in text for w in ["sad", "tired", "alone", "bad"]):
        return "sad"
    if any(w in text for w in ["happy", "great", "awesome", "love"]):
        return "happy"
    if any(w in text for w in ["angry", "mad", "annoyed"]):
        return "angry"

    return "neutral"
