import requests
from bs4 import BeautifulSoup


def btc_scraping():
    # Link of the web used
    try:
        start_url = 'https://www.infodolar.com/cotizacion-dolar-blue.aspx'
        # download the info in htm type and process it
        downloaded_html = requests.get(start_url)
        soup = BeautifulSoup(downloaded_html.text, "html.parser")
        # search for the selected selector and convert it to string so we use it
        full_table = soup.select('table.cotizaciones td')[2]
        full_string = full_table.text.split()
        prize = float(full_string[1].replace(',','.'))
    except:
        return ""

    return prize
