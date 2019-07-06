import telebot
from telebot import types
import db

bot = telebot.TeleBot('876278188:AAHd3rosfGrLD6gYpC96QB0s8L17s-2pQMg')

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Cоздать напоминание']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Мои напоминалки']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['удалить напоминание']])
    bot.send_message(message.chat.id, 'Wake me Up', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Cоздать напоминание':
        bot.send_message(message.chat.id, 'Введите текст для вашей напоминалки')
        bot.register_next_step_handler(message, get_text);  # следующий шаг – функция get_text
    elif message.text == 'Мои напоминалки':
        bot.send_message(message.chat.id, db)
    elif message.text == 'удалить напоминание':
        bot.send_message(message.chat.id, 'кнопка в разработке')

def murk_up():
    markup = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='клац', callback_data='bt_1')
    markup.add(bt_1)
def get_text(message): #получаем text
    global g_text, g_message_id
    g_message_id = message.chat.id
    g_text = message.text
    bot.send_message(message.from_user.id, 'когда вам это напомнить?')
    bot.register_next_step_handler(message, get_time)
def get_time(message):
    global g_time
    g_time = message.text
    bot.send_message(message.chat.id, 'напоминалка создана')
    markup = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='клац', callback_data='bt_1')
    markup.add(bt_1)
    bot.send_message(message.chat.id, 'для подтверждения-> клац', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'bt_1':
        data = (g_message_id, g_text, g_time)
        db.db(data)

bot.polling(none_stop=True)