def take_action(client, message, reason):
    if reason == "spam":
        message.delete()
