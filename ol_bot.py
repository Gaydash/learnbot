
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

#MessageHandler - obrabotchik soobsheniy
#CommandHandler -

# PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
#          'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'ol_bot.log'
                    )

def greet_user(ol_bot, update):
    text = 'Called command /start'
    logging.info(text)
    update.message.reply_text(text)

#def talk_to_me(ol_bot, update):
#    user_text = "Hi {}! You wrote: {}".format(update.message.chat.username, update.message.text)
#    logging.info("User: %s, chat id: %s, Message %s".update.message.chat.username, update.message.chat.id, update,message.chat.text)
#    print (user_text)
#    update.message.reply_text(user_text)
# logging.info('User: {}, chat id: {}'.format(update.message.chat.username, update.message.id))

def talk_to_me(ol_bot, update):
    user_text = 'Hi {}! You wrote: {}'.format(update.message.chat.username, update.message.text)
    user_text1 = 'User: {}, chat id: {}'.format(update.message.chat.username, update.message.chat.id)
    logging.info(user_text1)
    logging.info('User: %s, chat id: %s, Message %s', update.message.chat.username, update.message.chat.id, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Bot was started')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()