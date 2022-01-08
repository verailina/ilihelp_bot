import logging
from pathlib import Path

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler

from ilihelp_bot.gsheet_data import save_note


def get_token() -> str:
    with Path("token").open() as token_file:
        token = token_file.readline()

    return token

updater = Updater(token=get_token(), use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Note',
            input_message_content=InputTextMessageContent(query)
        )
    )
    save_note(query)
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps, run_async=True)
dispatcher.add_handler(inline_caps_handler)



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def note(update, context):
    print(context.args)




caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(CommandHandler("note", note))

updater.start_polling()
