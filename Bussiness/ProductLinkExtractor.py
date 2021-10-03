import Domain.preProcess
from bs4 import BeautifulSoup
import requests
import Utility.HTMLMaker

def loweringEnglishWord(string):
    strList = list(string)
    alphabetString = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, len(strList)):
        if strList[i] in alphabetString:
            strList[i] = strList[i].lower()
    return "".join(strList)

def hasProductStringAccept(productString):
    productString = loweringEnglishWord(productString)
    for string in Domain.preProcess.categorie_product_special_str:
        if string in productString:
            return True
    return False

def eligibleProductLink(url):
    print('Bussiness.productLinkExtractor.eligibleProductLink')
    html = Utility.HTMLMaker.htmlMaker(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    linksInPage = {}
    for link in bs.find_all('a'):
        if hasProductStringAccept(link.text):
            print(link.get_text().strip())
            try:
                linksInPage.update({link.get_text().strip():link['href']})
            except:
                continue
    return linksInPage

