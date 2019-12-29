import telebot

bot = telebot.TeleBot('975958816:AAGLi7yZgMErf3EwgaapEwSkBgufKurlQnk')

answ = '';
name = '';
surname = '';
age = 0;


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');


def get_name(message):  # получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);


def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);


def get_age(message):
    global age;
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '? (Y/N)');
    bot.register_next_step_handler(message, get_answ);


def get_answ(message):
    global answ;
    global age;
    global name;
    global surname;
    answ = message.text;

    if message.text == 'Y':
        bot.send_message(message.from_user.id, "Nice!");
        f = open('text.txt', 'w')
        f.write(str(age));
        f.write(str(name));
        f.close()
    elif message.text == 'N':
        bot.send_message(message.from_user.id, "Fuck!");
    else:
        bot.send_message(message.from_user.id, 'Fuck you!');


bot.polling(none_stop=True, interval=0)