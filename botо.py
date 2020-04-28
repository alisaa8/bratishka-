import telebot

bot = telebot.TeleBot('1256818903:AAGKBIpiOOKNZJiXODP5v6BOpGGHnGazaTA')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Семь на восемь', 'Восемь на семь')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')


bot.polling()


