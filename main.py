import telebot

bot = telebot.TeleBot('975958816:AAGLi7yZgMErf3EwgaapEwSkBgufKurlQnk')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, що нового ?')




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привіт':
        bot.send_message(message.chat.id, 'Привіт, ти мій творець ?')
    elif message.text == 'бувай' or message.text == 'папа':
        bot.send_message(message.chat.id, 'Бувай, папа, аліведерчі')
    else:
        bot.send_message(message.chat.id, 'Га, що, нашо ?')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')


bot.polling()
