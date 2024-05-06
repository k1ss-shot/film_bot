import telebot
from telebot import types

token = '7184101007:AAG5GVjlyr8eVd8MqQYS1PIOXh2f6IZY4qE'

bot = telebot.TeleBot(token=token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Салам алейкум, film bot приветсвует вас!')

    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Фантастика/фэнтези')
    btn2 = types.KeyboardButton('Детектив/Триллеры')
    btn3 = types.KeyboardButton('Боевики')
    btn4 = types.KeyboardButton('Ужасы')
    btn5 = types.KeyboardButton('Мультфильмы')
    btn6 = types.KeyboardButton('Драма/мелодрама')
    btn7 = types.KeyboardButton('Комедии')
    btn8 = types.KeyboardButton('Сериалы')
    btn9 = types.KeyboardButton('Аниме')
    btn10 = types.KeyboardButton('Документальные')
    btn11 = types.KeyboardButton('Подборки')
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    
    bot.send_message(message.chat.id, 'Выберите жанр фильма', reply_markup=markup)
        
        
bot.polling()