import json
import telebot
from drvWebScraping import btc_scraping
import schedule
import time
import asyncio

usuarios={}
usuarios['manu']='5178063489'
usd_prize=0

# we are reading the token from the environmental variables of the OS
file= open('settings.json')
settings = json.load(file)

#BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN=settings['TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
async def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

    
@bot.message_handler(commands=['dollar'])
async def send_welcome(message):
    usd_prize = btc_scraping()
    user=message.chat.first_name
    text = 'Hi ' +user+ ', the prize of the usd is ' + str(usd_prize)
    bot.reply_to(message, text)


@bot.message_handler(func=lambda msg: True)
async def echo_all(message):
    bot.reply_to(message, message.text)

def checkDolar():
    global usd_prize
    act_prize=btc_scraping()
    if act_prize != usd_prize :
        usd_prize=act_prize
        bot.send_message(usuarios['manu'],str(usd_prize))        

# After every 5 to 10mins in between run work()
schedule.every(1).minutes.do(checkDolar)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    #bot.infinity_polling()
    schedule.run_pending()
    time.sleep(1)