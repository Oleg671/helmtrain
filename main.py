import telebot

token='8161978023:AAGOm1EDAzf8tPhO16fwk3ZUNKOUs7TEP9Y'
bot = telebot.TeleBot(token)
GROUP_ID=-1002436277970
blacklist=["паучья", "хавальник","пауки", "паук", "призрачная", "эмилия", "ната", "щетинина", "берсика","берсику", "берсик", "нико", "админка", "шейминг", "закон", "законом", "ук", "украли", "украсть", "клевета", "паучьей", "баните", "отпишитесь", "отписаться", "подписчики", "эмилии", "срач", "шлюха", "пизда", "пиздец", "нахуй", "хуй", "шалава", "вагина"]
@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg=message.text.lower()
    for x in blacklist:
        if(x in msg.split(' ')):
            bot.delete_message(message.chat.id, message.message_id)
            print("Message:", message.message_id, "-",message.text, message.from_user)
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
