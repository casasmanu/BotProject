import mysql.connector
# We are going to define certain functions to communicate with a database
# first we define the connector, for now will be root but in the future each user should connect only to his data
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4684",
    database="mangateca"
)

mycursor = db.cursor()

#function to instert data in the manga database, as is going to be only 1 database and the info is limited, most of the values are hardcoded
def sqlInsert(input=[]):
    name=input[0]
    volumen=input[1]
    author=input[2]
    editorial=input[3]
    mycursor.execute("INSERT INTO manga(manga_name,volumen,author,editorial) VALUES (%s,%s,%s,%s)", (name,volumen,author,editorial))
    db.commit()

#function to delete certain volumen of a manga
def sqlDelete(input=[]):
    mycursor.execute("DELETE FROM manga WHERE manga_name=%s AND volumen=%s ;", (input[0],input[1]))
    db.commit()

#function to consult to our database which tomos do we have from that manga
def sqlConsult(manga):
    mycursor.execute("Select * FROM manga WHERE manga_name=%s", manga)
    db.commit()
