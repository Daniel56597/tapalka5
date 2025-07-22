from telebot import TeleBot, types

bot = TeleBot{'Token for the bot Тапалка @tapalkacarbot has been revoked. New token is:7567337505:AAFoDRKPW-PcpX7E1CL3JdVCibxxCy0HvKc'}

@bot.message_handler(commands=['start'])
def send_url_button(message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Открыть Тапалку", url="https://example.com")
    keyboard.add(btn)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы открыть сайт:", reply_markup=keyboard)

bot.polling()
