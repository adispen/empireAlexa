import urllib2
from bs4 import BeautifulSoup


def get_tonights_lights():
    quotePage = 'http://www.esbnyc.com/explore/tower-lights'
    page = urllib2.urlopen(quotePage)
    soup = BeautifulSoup(page, 'html.parser')
    lights = soup.find_all('h1', attrs={'class': 'title'})[1]
    return lights.text
