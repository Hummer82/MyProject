import telebot
from datetime import datetime

bot = telebot.TeleBot('6513613001:AAHZZ4GtQwRXpctL7L_KHasq1QRToDX-UY8')

@bot.message_handler(commands=['me'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['start'])
def main(message):
    user_id = message.from_user.id
    strtext = f'Команда Реклама Центра рада приветствовать Вас:\n<b>{message.from_user.first_name} {message.from_user.last_name}</b>\n<a href="/work">Задания</a>'
    bot.send_message(message.chat.id, strtext, parse_mode='html')

@bot.message_handler(commands=['login'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['work'])
def main(message):
    strdate = datetime.fromtimestamp(message.date).strftime("%d-%m-%Y %H:%M")
    bot.send_message(message.chat.id, f'Задания для <b>"ID:{message.from_user.id}</b> - {message.from_user.username}" {message.from_user.first_name} {message.from_user.last_name} на {strdate}', parse_mode='html')

bot.polling(none_stop=True)