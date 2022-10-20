from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def bot_hi(update: Update, context: ContextTypes.DEFAULT_TYPE) :
     await update.message.reply_text(f'Привет {update.effective_user.first_name}!')


async def bot_time(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text(f'сейчас {datetime.datetime.naw().time()}!')


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text(f'/Hi\n/time\n/help\n/sum')


async def bot_sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')
