from telegram.ext import Updater, InlineQueryHandler,MessageHandler, CommandHandler,Filters
import os
from botIPC import bind
import telegram
socket = bind();
T_TOKEN = os.getenv("T_TOKEN")
CHAT_ID = -495783570
def send_message(update,context):
    message_string = "from : " + update.message.from_user.first_name+"\n"+update.message.text
    
    socket.send_string(message_string)

def main():
    updater = Updater(T_TOKEN,use_context=True)
    dp = updater.dispatcher
    bot = updater.dispatcher.bot
    dp.add_handler(MessageHandler(Filters.text,send_message))
    updater.start_polling()
    while True:
        msg = socket.recv().decode("UTF-8");
        bot.sendMessage(chat_id=CHAT_ID, text=msg) 

if __name__ == '__main__':
    main()

