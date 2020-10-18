import telebot
from settings import BOT_TOKEN

# TODO: добавить logger

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    print(f'{message.from_user.username}:{message.text}')
    bot.send_message(message.from_user.id, "Ди на хуй")


bot.polling(none_stop=True, interval=0)
