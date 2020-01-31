import telebot

bot = telebot.TeleBot('#сюда токен')

client_base = []

keyboard_admin_1 = telebot.types.ReplyKeyboardMarkup()
keyboard_admin_1.row("Создать заказ")
keyboard_admin_1.row("Курьер едет", "Еда приехала")


inline_kb1 = telebot.types.InlineKeyboardMarkup()
inline_btn_1 = telebot.types.InlineKeyboardButton(text='Заказать', callback_data='cb_yes')
inline_btn_2 = telebot.types.InlineKeyboardButton(text='Отказаться', callback_data='cb_no')
inline_kb1.add(inline_btn_1, inline_btn_2)


@bot.message_handler(commands=['start'])
def start_message(message):
    global chat_id, admin_id, user_username
    chat_id = message.chat.id
    user_username = message.from_user.username
    if  user_username == 'Kychrey':
        admin_id = chat_id
        bot.send_message(message.chat.id, "Привет, хозяин. Какие ваши команды?", reply_markup=keyboard_admin_1)
    else:
        user_name = message.from_user.first_name
        client_base.append(chat_id)
        bot.send_message(message.chat.id, "Бип..Бип.. Обнаружена жизнь. Привет, " + user_name + 
                         ". Когда будут заказы, я сообщу!")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_username = message.from_user.username
    if user_username == 'Kychrey':
        if message.text == "Создать заказ":
            bot.send_message(message.chat.id, "Сколько комплектов есть?")
            bot.register_next_step_handler(message, get_order)
        elif message.text == "Курьер едет":
            for i in range(len(client_base)):
                bot.send_message(client_base[i], 'Курьер выехал! Примерное время ожидание 1 час!')
        elif message.text == "Еда приехала":
            for i in range(len(client_base)):
                bot.send_message(client_base[i], 'Курочка приехала! Место встречи - у Ждуна!')

        
        
def get_order(message):
    global order_num, count_num
    order_num = int(message.text)
    count_num = order_num
    bot.send_message(message.chat.id, 'Партия на ' + str(order_num) + ' комплектов создана.')
    for i in range(len(client_base)):
        bot.send_message(client_base[i], 'Доброе утро! Начинаю приём заказов, доступно: ' + str(order_num),
                          reply_markup=inline_kb1)
               
        
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global order_num
    if call.data == "cb_yes":
        if order_num != 0:
            order_num -= 1
            bot.send_message(call.message.chat.id, 'Ваш заказ принят, спасибо!')
            bot.send_message(call.message.chat.id, 'Вы можете оплатить заранее через Сбербанк Онлайн:'
                             ' на номер 79148228892 (Кычкин А.И)')
            bot.send_message(admin_id, str(count_num-order_num) + ') ' + str(call.from_user.username) + 
                             ' сделал заказ! Осталось ' + str(order_num) + ' комплектов!')
        else:
            bot.send_message(call.message.chat.id, 'К сожалению, курочек не осталось!') 
    elif call.data == "cb_no":
        bot.send_message(call.message.chat.id, 'Ну чтож, значит в следующий раз!')
        
        
bot.polling(none_stop=True, interval=0)
