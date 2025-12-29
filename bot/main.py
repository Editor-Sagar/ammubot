import asyncio
from pyrogram import Client
from bot.router import handle_message
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "ammu_bot",
    bot_token=BOT_TOKEN
)

@app.on_message()
async def handle(client, message):
    await handle_message(client, message)


async def main():
    await app.start()
    print("🤖 Bot started successfully")
    await idle()

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
