from pyrogram import Client
from bot.router import handle_message

app = Client("ammu_bot")

@app.on_message()
def main_handler(client, message):
    handle_message(client, message)

def main():
    app.run()
