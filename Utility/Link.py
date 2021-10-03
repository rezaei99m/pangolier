import requests
import re
import Domain.preProcess
from urllib.parse import urlparse
from urllib.parse import urljoin
import Utility.HTMLMaker
import Utility.HTMLMaker
from bs4 import BeautifulSoup
import Utility.Link
from unidecode import unidecode

def linkRepairer(unknownURL):
    """Convert static or relative link into static link"""
    return urljoin('{}'.format(Domain.preProcess.url), unknownURL)

def nextPage(url, currentPageNumber: str):
    """Important: the argument currentPageNumber must be a str"""
    html = Utility.HTMLMaker.htmlMaker(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    for link in bs.find_all('a'):
        if link.parent.name == 'li':
            if len(link.get_text()) == 1 and link.get_text().isdigit() and currentPageNumber != unidecode(link.get_text()):
                print(link.get_text())
                nextPageLink = link['href']
                return linkRepairer(nextPageLink)
