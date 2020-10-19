import telebot
import collections
from settings import BOT_TOKEN

# TODO: добавить logger

def remember():
    answer = yield "Я слушаю)"
    buffer[answer.from_user.id] = answer.text
    return answer.text


bot = telebot.TeleBot(BOT_TOKEN)
handlers = collections.defaultdict(remember)
buffer = collections.defaultdict(lambda: 'empty')


@bot.message_handler(commands=['remember'])
def remember_handler(message):
    print(f'{message.from_user.username}:{message.text}')
    telegram_id = message.from_user.id

    answer = next(handlers[telegram_id])
    # отправляем полученный ответ пользователю
    bot.send_message(chat_id=telegram_id, text=answer)


@bot.message_handler(content_types=['text'])
def insult(message):
    print(f'{message.from_user.username}:{message.text}')
    telegram_id = message.from_user.id
    if telegram_id in handlers:
        # если диалог уже начат, то надо использовать .send(), чтобы
        # передать в генератор ответ пользователя
        try:
            handlers[telegram_id].send(message)
        except StopIteration:
            del handlers[telegram_id]
            bot.send_message(chat_id=telegram_id, text=buffer[telegram_id])
            del buffer[telegram_id]
            bot.send_message(chat_id=telegram_id, text="Я канеш запомнил, но ты все равно идешь нахуй.")
            return
    bot.send_message(telegram_id, "Ди на хуй")


if __name__ == '__main__':
    # bot.polling(none_stop=True, interval=1)
    bot.start_polling()
    bot.idle()
