import json
from drvWebScraping import btc_scraping
import schedule
import time
from drvTelegram import bot_send_msg, getNewUsers
import numpy as np

usd_prize = 0
arrUsers = []


# update destinatary list
def updateDestinataryList():
    global arrUsers
    global jsonUsers
    arrTempUsers = []
    # read the json file and update the variable
    users_file = open('destinatorsList.txt', 'r+',encoding='utf-8')
    users_lines = users_file.readlines()
    users_file.close()
    #################################################
    # first take the vector with our users in the txt
    for i in users_lines:
        text = i.replace('\n', '')
        tupla = text.split(' ')
        arrTempUsers.append(tupla)

    ####### then read the requests for new users#######
    arrNewTelegramUsers = getNewUsers(BOT_TOKEN)

    ids = [row[1] for row in arrTempUsers]
    ######### append - unify both lists ##############
    for newuser in arrNewTelegramUsers:
        if newuser[1] not in ids:
            arrTempUsers.append(newuser)

    filterData = np.array(arrTempUsers)
    # now, with both lists in the same one, save it
    # in the txt and then replace the variable
    filterData=np.unique(filterData,axis=0)
    ############ WRITE VARIABLE IN THE TXT ########
    users_file = open('destinatorsList.txt', 'w',encoding='utf-8')
    for line in filterData:
        users_file.write(" ".join(line) + "\n")
    users_file.close()
    # replace the global variable with the temporal one
    if len(filterData) != len(arrUsers):
        arrUsers = filterData


def checkDolar():
    global usd_prize
    global arrUsers
    act_prize = btc_scraping()
    if act_prize != usd_prize:
        usd_prize = act_prize
        # update dolar for every registered user
        for user in arrUsers:
            bot_send_msg(BOT_TOKEN, user[1], str(usd_prize))


# we are reading the token from the environmental variables of the OS, load initial settings
file = open('settings.json')
settings = json.load(file)
BOT_TOKEN = settings['TOKEN']
updateDestinataryList()

# After every 5 to 10mins in between run work()
schedule.every(5).minutes.do(checkDolar)
schedule.every(12).hours.do(updateDestinataryList)
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
