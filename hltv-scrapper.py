import requests
from bs4 import BeautifulSoup
from datetime import datetime


def mountGameDict(game, datePreFormated):
    return {'event': {'name': game.select('.event-name')[0].text, 'img': game.select('.event img')[0]['src']},'teams': [{'name':game.select('.team')[0].text,'logo':game.select('.team-cell img')[0]['src']},{'name':game.select('.team')[1].text,'logo': game.select('.team-cell img')[1]['src']}], 'date': datePreFormated.strftime('%Y-%m-%d %H:%M'),'type':game.select('.map-text')[0].text}

def getTodayMatches():
    page = requests.get('https://www.hltv.org/matches')
    html = BeautifulSoup(page.content,'html5lib')
    dateNow = datetime.now().strftime('%Y-%m-%d')
    arr = []
    for game in html.select('.match-day table'):
        timestamp = int(game.select('div.time')[0].get('data-unix'))
        datePreFormated = datetime.fromtimestamp(timestamp/1000)
        dateFormated = datePreFormated.strftime('%Y-%m-%d')
        if dateFormated == dateNow:
            arr.append(mountGameDict(game, datePreFormated))
    return arr
            

def getMatchesByDate(date):
    page = requests.get('https://www.hltv.org/matches')
    html = BeautifulSoup(page.content,'html5lib')
    dateNow = datetime.now().strftime('%Y-%m-%d')
    arr = []
    for game in html.select('.match-day table'):
        timestamp = int(game.select('div.time')[0].get('data-unix'))
        datePreFormated = datetime.fromtimestamp(timestamp/1000)
        dateFormated = datePreFormated.strftime('%Y-%m-%d')
        if dateFormated == date:
            arr.append(mountGameDict(game, datePreFormated))
    return arr

print(getTodayMatches())