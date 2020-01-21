import telebot

bot = telebot.TeleBot('1047866872:AAFnCzFOTVwmFPn_zIaxpfntXqxaH3S28S8')

#Клавиатуры###############################################################
keyboard_1 = telebot.types.ReplyKeyboardMarkup()
keyboard_1.row('Сделать заказ', 'Пока')

keyboard_admin_1 = telebot.types.ReplyKeyboardMarkup()
keyboard_admin_1.row('Создать заказ', 'Свободные курочки')
##########################################################################

users = []

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.username
    if user == 'kychrey':
        bot.send_message(message.chat.id, 'Привет, хозяин! Что нужно сделать?', reply_markup=keyboard_admin_1)
    else:
        users.append(user)
        bot.send_message(message.chat.id, 'Бип..Бип.. Обнаружена живая форма жизни. Выберите команду.', reply_markup=keyboard_1)
        

@bot.message_handler(content_types=['text'])
def admin_menu(message):
    if user == 'kychrey':
        if message.text.lower() == 'Создать заказ':
            bot.send_message(message.chat.id, 'Создаю заказ. Сколько наборов есть?')
            bot.register_next_step_handler(message, get_order);
        if message.text.lower() == 'Свободные курочки':
            bot.send_message(message.chat.id, 'Сколько курочек осталось?')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы не мой хозяин')
        
def get_order(message): #получаем кол-во заказов
    global order;
    order = message.text;
    bot.send_message(message.from_user.id, 'Создаю ' + order + 'заказов');
    bot.register_next_step_handler(message, get_surnme);
    


bot.polling()

