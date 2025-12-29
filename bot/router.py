from bot.ai.ai_reply import ai_reply
from bot.moderation.anti_spam import is_spam
from bot.moderation.auto_action import take_action

def handle_message(client, message):
    text = message.text or ""

    if is_spam(message.from_user.id):
        take_action(client, message, "spam")
        return

    reply = ai_reply(text)
    message.reply_text(reply)
