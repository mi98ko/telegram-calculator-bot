from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        expression = update.message.text
        result = eval(expression)
        await update.message.reply_text(f"Result: {result}")
    except:
        await update.message.reply_text("Invalid ❌")

app = ApplicationBuilder().token("8789915746:AAEv73rLP8X87dD900lTVqY9AATs7_dINa4").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()
