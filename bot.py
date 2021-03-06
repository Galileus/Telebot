import telebot
import config
import pb
import datetime
import pytz
import json
import traceback



P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)
####################################################################################
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Greetings! I can show you exchange rates.\n' +
        'To get the exchange rates press /exchange.\n' +
        'To get help press /help.'
  )
##############################################################################################
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/Galileys'
  )
    )
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' +
        '2) Click on the currency you are interested in.\n' +
        '3) You will receive a message containing information regarding the source and the target currencies, ' +
        'buying rates and selling rates.\n' +
        '4) Click “Update” to receive the current information regarding the request. ' +
        'The bot will also show the difference between the previous and the current exchange rates.\n' +
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=keyboard
    )
#########################################################################################
@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('menu', url='telegram.me/Galileys'))
    bot.send_message(message.chat.id, 'here you can find the menu for this bot', reply_markup=keyboard)
##########################################################################################
if __name__ == '__main__':
    bot.polling(none_stop=True)
