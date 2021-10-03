import Bussiness.ProductInformationExtractor
import json
from elasticsearch import Elasticsearch

def saveJSON(fileName, linkOfProduct, productName):
    with open('D:\\Files\\Projects\\WebScrapping\\Data\\{}.json'.format(str(fileName)), 'w', encoding='utf-8') as json_file:
        json.dump(Bussiness.ProductInformationExtractor.productInformationExtractor(linkOfProduct, productName), json_file, ensure_ascii=False) 

def _countFeatures(json):
    """json must be name of the json file link a.json"""
    keyCounter = 0
    with open('{}'.format(json)) as json_file:
        data = json.load(json_file)
        for key, value in data:
            print('The key is ' + str(key) + ' and the value is ' + str(value))
            keyCounter += 1
    return keyCounter

def saveToElasticSearch(index, doc_type, id, body):
    es = Elasticsearch()
    es.index(index=str(index), doc_type=str(doc_type), id=id, body=body)