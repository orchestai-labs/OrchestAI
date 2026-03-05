from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from core.orchestrator import handle_task

TOKEN = "8668471035:AAEnIPraBvKXPmh3s0fAC3ARdLky8dhg7C8"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text

    response = handle_task(user_message)

    await update.message.reply_text(response)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("OrchestAI Telegram Bot Running...")

app.run_polling()