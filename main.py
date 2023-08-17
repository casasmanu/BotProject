import json
import telebot
from drvWebScraping import btc_scraping
import schedule
import time
import asyncio

usuarios={}
usuarios['manu']='5178063489'
usd_prize=0
users_file= open('destinatorsList.json')
data=json.load(users_file)
arrUsers=[]

for i in data["users"]:
    arrUsers.append(i)
print(arrUsers)

# we are reading the token from the environmental variables of the OS
file= open('settings.json')
settings = json.load(file)

#BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN=settings['TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)

def bot_send_msg(id,msg):
    bot.send_message(id,msg)      

def checkDolar():
    global usd_prize
    global arrUsers
    act_prize=btc_scraping()
    if act_prize != usd_prize :
        usd_prize=act_prize
        #update dolar for every registered user
        for user in arrUsers:
            bot_send_msg(user["id"],str(usd_prize))

# After every 5 to 10mins in between run work()
schedule.every(5).minutes.do(checkDolar)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    #bot.infinity_polling()
    checkDolar()
    schedule.run_pending()
    time.sleep(1)