import telebot
from datetime import datetime
import pytz, re

moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))

token='8161978023:AAGOm1EDAzf8tPhO16fwk3ZUNKOUs7TEP9Y'
bot = telebot.TeleBot(token)
GROUP_ID=[-1002324488081,-1002325350087, -1002436277970] #ПЛ болт ирис
list_hot=['нюд']
regex = r"(?:https?:\/\/(?:[\w-]+\.)+[a-z]{2,}|www\.[a-z0-9-]+.[\w-]+(?:[\/\\\?][^\s]*)?)"
prep=punctuation_marks = ['.',',','!','?',':',';','(',')','[',']','{','}','...','“','”','‘','’','—','–']
with open('./codeWords.txt', encoding='utf-8') as f:
    blacklist = f.read().split(' ')
@bot.message_handler(content_types=['text'])
@bot.channel_post_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['any'])
def handle_edited_messages(message):
    if message.from_user.id!=1087968824:
        delfunc(message)
def handle_channel_post(message):
    if message.from_user.id!=1087968824:
        delfunc(message)
def handle_text(message):
    if message.from_user.id!=1087968824:
        delfunc(message)




def delfunc(message):
    msg=message.text.lower()
    # links = re.findall(regex, msg)
    links =re.findall(regex, message.html_text)
    if message.link_preview_options:
        tmp=re.findall(regex,message.link_preview_options.url)
        links+=re.findall(regex,message.link_preview_options.url)
    todel=True
    if links:
        for i in range(len(links)):
            if links[i]=="https://www.avito.ru":
                todel=False
            else:
                todel=True
        if todel:
            bot.delete_message(message.chat.id, message.message_id)
            print(datetime.now(pytz.timezone('Europe/Moscow')), "Message:", message.message_id, "-",message.text, message.from_user)
            pass
    for i in range(len(prep)):
        msg=msg.replace(prep[i],'')
    for y in list_hot:
        if(y in msg.split(' ') and message.chat.id in GROUP_ID and "#продажа" in msg.split(' ')):
            bot.forward_message(1835147179, message.chat.id, message.message_id)
    for x in blacklist:
        if(x in msg.split(' ') and message.chat.id in GROUP_ID):
            bot.delete_message(message.chat.id, message.message_id)
            print(datetime.now(pytz.timezone('Europe/Moscow')), "Message:", message.message_id, "-",message.text, message.from_user)
        elif message.chat.id not in GROUP_ID:
            info = "ChatID: "+str(message.chat.id)+"\nMessage: "+str(message.message_id)+" - "+str(message.text)+"\nFrom: "+str(message.from_user)
            bot.forward_message(1835147179, message.chat.id, message.message_id)
            bot.send_message(1835147179,info)
            break
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
