from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('hello, this is punk bot')
    print(context)
    print('\n\n\n\n')
    print(update)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton('Option1', callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f'{update.message.text[::-1]}', reply_to_message_id=update.message.id, reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    match query.data:
        case '1':
            await query.answer()
            await query.edit_message_text('success')


def main():
    application = ApplicationBuilder().token('insert telegram bot api token here').build()

    application.add_handler(CommandHandler('start', start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


if __name__ == "__main__":
    main()
