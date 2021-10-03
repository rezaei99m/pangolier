import requests
from bs4 import BeautifulSoup
import datetime
import Utility.HTMLMaker

# return True if it finds a search bar + the class name of that search bar & return False it doesn't find one
def findSearchBar(url):
    print('Bussiness.SearchBar.findSearchBar')
    html = Utility.HTMLMaker.htmlMaker(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    try:
        if bs.find('input') != None and bs.find('input').attrs['placeholder'] != None:
            return bs.find('input').attrs['class']
        else:
            return False
    except:
        # print('oh shit')
        return False