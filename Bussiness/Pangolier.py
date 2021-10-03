import ProductInformationExtractor
import ProductLinkExtractor
import SearchBar
import SearchCategory

from Domain import preProcess
from Utility import Link

from Utility.save import saveJSON as saveJSON
from Utility.save import saveToElasticSearch as saveToElasticSearch
from elasticsearch import Elasticsearch
import json


def start():
    counter_json = 0
    counter_product_crawl = 0
    pageNumber = 1
    prodcutList = []
    prodcutUrlPages = ''
    if SearchBar.findSearchBar(preProcess.url):
        resultPageOfSearchingCategory = SearchCategory.searchCategory(preProcess.url)
        while counter_product_crawl < preProcess.howManyProductToSearch:
            print('The page number is : ' + str(pageNumber))
            if pageNumber == 1:
                linksAndNamesOfProduct = ProductLinkExtractor.eligibleProductLink(resultPageOfSearchingCategory)
                prodcutUrlPages = resultPageOfSearchingCategory
            else:
                print('enter here' )
                linksAndNamesOfProduct = ProductLinkExtractor.eligibleProductLink(Link.nextPage(prodcutUrlPages, str(pageNumber - 1)))
                prodcutUrlPages = Link.nextPage(prodcutUrlPages, str(pageNumber - 1))
            for productLink in linksAndNamesOfProduct.values():
                productName = ''
                link = Link.linkRepairer(productLink)
                for nameOfProduct, linkOfProduct in linksAndNamesOfProduct.items():
                    if linkOfProduct == link:
                        productName = str(nameOfProduct)
                print(str(counter_product_crawl) + '    ' + str(link))
                if len(ProductInformationExtractor.productInformationExtractor(link, productName)) != 0:
                    # saveToElasticSearch('my_index2', 'x', counter_json, Bussiness.ProductInformationExtractor.productInformationExtractor(link, productName))
                    saveJSON(counter_json, link, productName)
                    counter_json += 1
                    counter_product_crawl += 1
            pageNumber += 1
    else:
        print('The website doesn\'t have any search bar')
    return prodcutList

start()