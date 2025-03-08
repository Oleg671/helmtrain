import telebot
from datetime import datetime
import pytz

moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))

token='8161978023:AAGOm1EDAzf8tPhO16fwk3ZUNKOUs7TEP9Y'
bot = telebot.TeleBot(token)
GROUP_ID=-1002324488081
blacklist=["паучья", "хавальник","пауки", "паук", "призрачная", "эмилия", "ната", "щетинина", "берсика","берсику", "берсик", "нико", "админка", "шейминг", "закон", "законом", "ук", "украли", "украсть", "клевета", "паучьей", "баните", "отпишитесь", "отписаться", "подписчики", "эмилии", "срач", "шлюха", "пизда", "пиздец", "нахуй", "хуй", "шалава", "вагина"]
@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg=message.text.lower()
    for x in blacklist:
        if(x in msg.split(' ') and message.chat.id==GROUP_ID):
            bot.delete_message(message.chat.id, message.message_id)
            print(datetime.now(pytz.timezone('Europe/Moscow')), "Message:", message.message_id, "-",message.text, message.from_user)
        elif message.chat.id!=GROUP_ID:
            info = "ChatID: "+str(message.chat.id)+"\nMessage: "+str(message.message_id)+" - "+str(message.text)+"\nFrom: "+str(message.from_user)
            bot.forward_message(1835147179, message.chat.id, message.message_id)
            bot.send_message(1835147179,info)
            break
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
