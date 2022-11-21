import telebot

bot = telebot.TeleBot("5920024885:AAGpZvjUKsZJlXtRhwsWt1xJ0yJ0ITwZxLo")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello, {message.from_user.first_name}"
    bot.send_message(message.chat.id, mess)


bot.polling(none_stop=True)