from django.shortcuts import render
import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL_BASE = "https://www.nbrb.by/api/exrates/rates?ondate="


def core_kurs_dollar(request):
    url = URL_BASE
    date = datetime.now().strftime("%y-%m-%d")
    periodicity = "&periodicity=0"
    data = requests.get(url + date + periodicity, params=locals()).json()
    kurs_dollar = data[5]['Cur_OfficialRate']
    return f'${kurs_dollar}'


def currency(request):
    url = URL_BASE
    date = datetime.now().strftime("%y-%m-%d")
    date_html = datetime.now().strftime("%d.%m.%y")
    periodicity = "&periodicity=0"
    data = requests.get(url + date + periodicity, params=locals()).json()
    dollar_nb = data[5]['Cur_OfficialRate']
    euro_nb = data[6]['Cur_OfficialRate']
    rosrubl_nb = data[17]['Cur_OfficialRate']
    link = "https://myfin.by/currency/minsk"
    text = requests.get(link, headers={'User-agent': 'Super Bot Power Level Over 9000'}).text
    soup = BeautifulSoup(text, 'html.parser')
    parser_all = soup.find_all('td')
    dollar_pok = parser_all[1].text.replace('\n', '')
    dollar_prod = parser_all[2].text.replace('\n', '')
    euro_pok = parser_all[6].text.replace('\n', '')
    euro_prod = parser_all[7].text.replace('\n', '')
    rosrubl_pok = parser_all[11].text.replace('\n', '')
    rosrubl_prod = parser_all[12].text.replace('\n', '')
    context = {'dollar_nb': dollar_nb, 'euro_nb': euro_nb,
               'rosrubl_nb': rosrubl_nb, 'date': date, 'date_html': date_html,
               'dollar_pok': dollar_pok, 'dollar_prod': dollar_prod,
               'euro_pok': euro_pok, 'euro_prod': euro_prod,
               'rosrubl_pok': rosrubl_pok, 'rosrubl_prod': rosrubl_prod,
               }
    return render(request, 'currency/currency.html', context)






