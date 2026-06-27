from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("8711228913:AAHq1q08zpramQBsd7dVGcZFFg6nh3ZfQyY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Merhaba!\n\n"
        "Ben Emre Crypto AI 🇹🇷\n\n"
        "Şunları sorabilirsin:\n"
        "• Bugün ne alabilirim?\n"
        "• BTC alınır mı?\n"
        "• En güçlü coinler"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "bugün ne alabilirim" in text:
        await update.message.reply_text(
            "📊 İlk sürüm aktif.\n\n"
            "Yakında canlı piyasa analizleri eklenecek."
        )
    else:
        await update.message.reply_text(
            "Sorunu anladım 👍\nYakında gelişmiş analiz sistemi eklenecek."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
