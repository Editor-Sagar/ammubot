import time
spam_log = {}

def is_spam(uid):
    now = time.time()
    spam_log.setdefault(uid, [])
    spam_log[uid] = [t for t in spam_log[uid] if now - t < 10]
    spam_log[uid].append(now)
    return len(spam_log[uid]) > 5
