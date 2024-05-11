import telebot
from telebot import types
from kinogo_biz_parse import get_film_list

token = '7184101007:AAG5GVjlyr8eVd8MqQYS1PIOXh2f6IZY4qE'

bot = telebot.TeleBot(token=token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Салам алейкум, film bot приветсвует вас!')

    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('показать список фильмов')
    
    markup.add(btn1)
    
    bot.send_message(message.chat.id, 'Выберите фильм', reply_markup=markup)

def send_bot_message(chat_id, film_list):
    for film in film_list:
        text =  f'`Название`: {film["name"]}\n'\
                f'{film["info"]}\n'\
                f'`Описание`: {film["description"]}\n'\
                f'[-------------------------------]({film["poster"]})'
    

        keyboard = types.InlineKeyboardMarkup()
        buttom_watch = types.InlineKeyboardButton(text='смотреть', url=film["url"])
        keyboard.add(buttom_watch)
        bot.send_message(chat_id=chat_id,
                         text=text,
                         parse_mode='Markdown',
                         reply_markup=keyboard)
    
        
@bot.message_handler(func=lambda message: message.text == 'показать список фильмов')
def show_film_list(message):
    film_list = get_film_list()
    send_bot_message(message.chat.id, film_list)

bot.polling()