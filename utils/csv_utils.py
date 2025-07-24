import csv, os
from datetime import datetime
from telegram import Bot

SIGNALS_DIR = "signals"
os.makedirs(SIGNALS_DIR, exist_ok=True)
CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

def log_signal(alarm_type, data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{SIGNALS_DIR}/signals_{date_str}.csv"
    new_file = not os.path.exists(file_path)
    row = [datetime.now().isoformat(), alarm_type, data]

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "alarm_type", "data"])
        w.writerow(row)

    with open(file_path, "r", encoding="utf-8") as f:
        if sum(1 for _ in f) >= 500:
            if BOT_TOKEN and CHAT_ID:
                Bot(token=BOT_TOKEN).send_document(chat_id=CHAT_ID, document=open(file_path, "rb"))
            os.remove(file_path)
