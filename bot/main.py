from pyrogram import Client, filters
from bot.router import handle_message

app = Client("ammu_bot", bot_token=os.getenv("BOT_TOKEN"))

@app.on_message(filters.text)
def main(client, message):
    handle_message(client, message)

app.run()
