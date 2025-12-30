from flask import Flask
from threading import Thread
from bot import start_bot   # your bot start function

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_bot():
    start_bot()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
