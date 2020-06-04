import telebot

bot = telebot.TeleBot("1161566875:AAGVkDw5fuhkFoBrjylfP36LVM8rkwe5jw4")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)
bot.polling( none_stop = True ) 

