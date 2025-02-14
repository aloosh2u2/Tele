import telebot

# Replace with your bot token (inside quotes)
TOKEN = "7752126316:AAGwoOk0OJum-6dR3qIV4VkugJzuFmsufU4"
bot = telebot.TeleBot(TOKEN)

# Replace with your actual Telegram user ID
ADMIN_ID = 907621844  # Example: 123456789

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! أرسل رسالتك أو رأيك بسرية.")

@bot.message_handler(func=lambda message: True)
def forward_feedback(message):
    bot.send_message(ADMIN_ID, f"📩 New Anonymous Feedback:\n\n{message.text}")
    bot.reply_to(message, "تم إرسال رسالتك السرية بنجاح✅")

print("Bot is running...")
bot.infinity_polling()
