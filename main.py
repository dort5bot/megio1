from telegram.ext import ApplicationBuilder
from keep_alive import keep_alive
from handlers.io_nls_npr_handler import register_handlers
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.getenv("PORT", 8080))

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    register_handlers(app)
    keep_alive()
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{os.getenv('KEEP_ALIVE_URL')}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
