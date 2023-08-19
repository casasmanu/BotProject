import telebot

#define usefull functions
def bot_send_msg(BOT_TOKEN,id,msg):
 bot = telebot.TeleBot(BOT_TOKEN)  
 bot.send_message(id,msg)
 return


def getNewUsers(BOT_TOKEN):
 bot = telebot.TeleBot(BOT_TOKEN)  
 arrRawData=bot.get_updates()
 arrIds=[]
 for i in arrRawData:
  arrIds.append([i.message.chat.first_name,str(i.message.from_user.id)])
 return arrIds

