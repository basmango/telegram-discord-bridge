from telegram.ext import Updater, MessageHandler, Filters
import os
from bot_ipc import bind
import telegram
socket = bind()
T_TOKEN = os.getenv("T_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(update, context):
    if(str(update.message.chat_id)!=CHAT_ID):return;
    message_string = "<**" + \
        update.message.from_user.first_name+"**> "+update.message.text

    socket.send_string(message_string)


def main():
    updater = Updater(T_TOKEN, use_context=True)
    dp = updater.dispatcher
    bot = updater.dispatcher.bot
    dp.add_handler(MessageHandler(Filters.text, send_message))
    updater.start_polling()
    while True:
        msg = socket.recv().decode("UTF-8")
        bot.sendMessage(chat_id=CHAT_ID, text=msg,parse_mode="Markdown")


if __name__ == '__main__':
    main()
