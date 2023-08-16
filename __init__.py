from drvWebScraping import btc_scraping

#if __name__ == '__main__':
#inicio el updater con el codigo token del bot
#a= btc_scraping() 
#while True:

from datetime import datetime 
date_time = datetime.now()
crr_time = int(date_time.strftime("%S"))
print("Current timestamp", crr_time)
old_time=int(date_time.strftime("%S"))


while True:
 date_time = datetime.now()
 crr_time = int(date_time.strftime("%S"))

 if (abs(crr_time-old_time) >= 5):
   print(crr_time)
   old_time=crr_time