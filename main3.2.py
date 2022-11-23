import telebot
from telebot import types

bot = telebot.TeleBot("5920024885:AAGpZvjUKsZJlXtRhwsWt1xJ0yJ0ITwZxLo")

print('Bot start')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    user_id = types.KeyboardButton('id')
    premka = types.KeyboardButton('subscribe')
    markup.add(user_id, premka)
    mess = f"Hello, {message.from_user.first_name}"
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler()
def user_info(message):
    user_id = f'{message.from_user.id}'
    premka = f'{message.from_user.is_premium}'
    if message.text =='id':
        bot.send_message(message.chat.id, user_id)
    if message.text =='subscribe':
        bot.send_message(message.chat.id, premka)




bot.polling(none_stop=True)
