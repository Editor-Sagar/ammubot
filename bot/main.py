import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.router import handle_message
from pyrogram import Client

app = Client("ammu_bot")

@app.on_message()
def main_handler(client, message):
    handle_message(client, message)

def main():
    app.run()
