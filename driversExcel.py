#excel Drivers
from email import header
from unicodedata import name
import pandas as pd

def addusertoexcel(mat:dict):
    tempDict=readexcel()
    tempDict[dict.keys]=dict.values
    savetoexcel(tempDict)


def savetoexcel(mat:dict):
    withitems=pd.DataFrame(mat.items(),columns=['Id','Nombre'])
    withitems.to_excel("C:/Users/manum/Documents/Codigo VS/telegrambot-btc/Data/saved_file.xlsx")

def readexcel():
    hardcodedPath="C:/Users/manum/Documents/Codigo VS/telegrambot-btc/Data/saved_file.xlsx"
    wbReaded = pd.read_excel(hardcodedPath)
    ids=wbReaded['Id']
    names=wbReaded['Nombre']
    #dict=wbReaded.to_dict(orient=0)
    for id in ids.count:
        dict[ids[id]]=names[id]
    #    dict[temp(0)]=temp(1)

    return dict

if __name__ == '__main__':
    #name 4 testing
    mydict={}
    mydict['5178063489']="manu"
    mydict['220619299']="jose"
    while True:
        a=readexcel()

#reads excel and adds value    
#hardcodedPath="/home/pi/Desktop/saved_file.xlsx"
#dict = pd.read_excel(hardcodedPath,usecols=['nombre','bot id'])

#print(dict.keys())
#mydict['new']="47686414"

#withitems=pd.DataFrame(mydict.items(),columns=['nombre','bot id'])
#withitems.to_excel('/home/pi/Desktop/saved_file.xlsx', index = False)