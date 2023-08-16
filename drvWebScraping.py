import requests
from bs4 import BeautifulSoup


def btc_scraping():
    # link de la fuente
    start_url = 'https://www.infodolar.com/cotizacion-dolar-blue.aspx'
    # descargo la info en html de la pagina y la parseo
    downloaded_html = requests.get(start_url)
    soup = BeautifulSoup(downloaded_html.text, "html.parser")
    # busco el selector deseado y lo convierto en string para su uso
    full_table = soup.select('table.cotizaciones td')[2]
    string = full_table.text.split()
    string = string[0] + string[1]

    format_result = string
    print(format_result)
    # print(format_result)
    return format_result

