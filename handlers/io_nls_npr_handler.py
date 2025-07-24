from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.binance_utils import get_io_report, get_nls_signal, get_npr_signal
from utils.csv_utils import log_signal

async def io(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = await get_io_report()
    await update.message.reply_text(report)

async def nls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pattern = " ".join(context.args).upper() if context.args else ""
    result = await get_nls_signal(pattern)
    log_signal("NLS", result)
    await update.message.reply_text(result)

async def npr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin = context.args[0].upper() if context.args else "BTC"
    result = await get_npr_signal(coin)
    log_signal("NPR", result)
    await update.message.reply_text(result)

def register_handlers(app):
    app.add_handler(CommandHandler("io", io))
    app.add_handler(CommandHandler("nls", nls))
    app.add_handler(CommandHandler("npr", npr))
