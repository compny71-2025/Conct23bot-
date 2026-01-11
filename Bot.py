import telebot

TOKEN = "8585009841:AAHP_hbBp20tPeLavfuwtZaH0X_gMMV12II"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ @Conct23bot يعمل على GitHub!")

print("🚀 البوت يبدأ...")
bot.polling()
