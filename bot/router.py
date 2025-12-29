from bot.personality.human_talk import human_reply
from bot.moderation.anti_spam import is_spam
from bot.moderation.auto_action import take_action

def handle_message(client, message):
    user = message.from_user
    text = message.text or ""
    first_name = user.first_name or "Friend"

    if is_spam(user.id):
        take_action(client, message, "spam")
        return

    reply = human_reply(text, first_name)
    message.reply_text(reply)
