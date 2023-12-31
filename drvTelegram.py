import telebot
import json

#define usefull functions
def bot_send_msg(BOT_TOKEN,id,msg):
 bot = telebot.TeleBot(BOT_TOKEN)  
 bot.send_message(id,msg)
 return


def getNewUsers(BOT_TOKEN):
 bot = telebot.TeleBot(BOT_TOKEN)  
 arrRawData=bot.get_updates()
 arrIds=[]
 
 try:
    for i in arrRawData:
      if(i.message!=""):
        #get important values from the msg
        userName=i.message.chat.first_name
        userId=str(i.message.from_user.id)
        #if the msg was already catched, skip to the next msg
        if(checkUserExistsInArray(arrIds,userId)):
            continue

        arrIds.append([userName,userId])
    return arrIds
 except Exception as error:
    # handle the exception
    print("An exception occurred:", error)

def checkUserExistsInArray(array,userId):
  output = False
  for i in array:
    if (i[1]==userId):
        output=True

  return output

