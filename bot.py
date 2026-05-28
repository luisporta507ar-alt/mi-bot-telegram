from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8835544562:AAGpgHQEulSISbsg__S_fweHltam06tGdJE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Soy tu bot 🤖\n\nPuedo responder:\n/hora - Ver la hora\n/ayuda - Ver comandos")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponibles:\n/start - Iniciar\n/ayuda - Esta
