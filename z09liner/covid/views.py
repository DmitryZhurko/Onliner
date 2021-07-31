from django.shortcuts import render
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def covid(request):
    link = "https://stopcovid.belta.by"
    text = requests.get(link).text
    parser = BeautifulSoup(text, 'html.parser')
    test_performed = parser.find_all('div', {'field': 'title'})
    test_performed_all = test_performed[0].text.replace('\n', '')
    test_performed_today = test_performed[1].text.replace('\n', '')

    registered = parser.find_all('div', {'field': 'title2'})
    registered_all = registered[0].text.replace('\n', '')
    registered_today = registered[1].text.replace('\n', '')

    discharged = parser.find_all('div', {'field': 'title3'})
    discharged_all = discharged[0].text.replace('\n', '')
    discharged_today = discharged[1].text.replace('\n', '')

    died = parser.find_all('div', {'field': 'title4'})
    died_all = died[0].text.replace('\n', '')
    died_today = died[1].text.replace('\n', '')

    date = datetime.now().strftime("%d.%m.%y")
    context = {'test_performed_all': test_performed_all, 'test_performed_today': test_performed_today,
               'registered_all': registered_all, 'registered_today': registered_today,
               'discharged_all': discharged_all, 'discharged_today': discharged_today,
               'died_all': died_all, 'died_today': died_today, 'date': date}
    return render(request, 'covid/covid.html', context)
