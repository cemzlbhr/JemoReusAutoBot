import telebot
import os

TOKEN = os.environ.get("7551513135:AAFI_by9EaoUdoPpaGPmNPhEejyZvS4-0a8")  # Heroku ortam değişkeni
bot = telebot.TeleBot(TOKEN)

# Her mesaja otomatik cevap
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, "Merhaba! Mesajınızı aldım, en kısa sürede döneceğim.")

print("Bot çalışıyor...")
bot.polling()
