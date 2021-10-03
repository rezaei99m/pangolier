import requests
from bs4 import BeautifulSoup
import Bussiness.ProductLinkExtractor
import Domain.preProcess
#  Domain.preProcess
import Utility.HTMLMaker
import json
from Utility.save import saveJSON as saveJSON

def hasProductStringAccept(productString):
    productString = Bussiness.ProductLinkExtractor.loweringEnglishWord(productString)
    for string in Domain.preProcess.categorie_features:
        if string in productString:
            return True
    return False

def productStringFilter(beautifulSoup):
    webPageText = []
    inputText = beautifulSoup.find_all(text=True)
    for tag in inputText:
        if tag.parent.name not in Domain.preProcess.tag_blackList:
            webPageText.append(tag.strip())
    for i in range(0, 10000000):
        try:
            webPageText.remove('')
        except:
            break
    return webPageText

def findingWhetherFeaturesAreRelated(productFeatureKey):
    productStringArray = productFeatureKey.split()
    for key in Domain.preProcess.laptop_features.keys():
        for item in productStringArray:
            if item == key:
                return True
    return False

def productInformationExtractor(url, nameOfProduct):
    """Getting inforamtion of product with their name"""
    html = Utility.HTMLMaker.htmlMaker(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    productFeatureList = productStringFilter(bs)
    productFeatureDict = {}
    productFeatureDict.update({'نام': '{}'.format(str(nameOfProduct))})
    # print('The name is : '+ '{}'.format(nameOfProduct) + "    " + str(type('{}'.format(nameOfProduct))))
    for i in range(0, len(productFeatureList) - 2):
        for feature in Domain.preProcess.categorie_features:
            if feature in productFeatureList[i]:
                if len(productFeatureList[i]) < 30:
                    j = i + 1
                    while j < len(productFeatureList) - 1:
                        if len(productFeatureList[j]) < 30:   
                            if findingWhetherFeaturesAreRelated(str(productFeatureList[i])):
                                productFeatureDict.update({'{}'.format(productFeatureList[i]): '{}'.format(productFeatureList[j])})
                                break
                        j += 1
    return productFeatureDict
