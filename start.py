from telegram.ext import Updater, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent


updater = Updater(token='1927613822:AAHBghOfy_F2odwCHYxMsUgWaHm4ncTD_qE', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)



updater.start_polling()