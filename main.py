import telebot

bot = telebot.TeleBot("7084336327:AAGLRNVkAtz65NVReQpJHEbi8iMEuAGgGo8")

@bot.message_handler()
def Myfunc(message):
    bot.send_message(message.chat.id, "Hi, What's happend?")




bot.infinity_polling(skip_pending=True)