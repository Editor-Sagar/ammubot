from bot.admin.admin_check import is_owner

def handle_secret(client, message):
    """
    Allows only owner to silently remove users.
    Usage: Reply /kick to a user's message.
    """
    if not is_owner(message.from_user.id):
        return

    if message.reply_to_message:
        try:
            client.ban_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
        except:
            pass
