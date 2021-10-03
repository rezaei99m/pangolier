import Bussiness.SearchBar
import Domain.preProcess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import Bussiness.ProductLinkExtractor
import numpy as np

def searchCategory(url):
    print('Bussiness.SearchCategory.searchCategory')
    inputClasses = Bussiness.SearchBar.findSearchBar('{}'.format(url))
    inputClass = ''
    for class_ in inputClasses:
        inputClass = inputClass + '{}'.format(class_) + ' '
    inputClass = inputClass.rstrip()
    driver = webdriver.Firefox()
    driver.get('{}'.format(Domain.preProcess.url))
    #TODO: Here i have to code implicit wait in order to check DOM as soon as search bar appears, then i have to check into it, and then wait also implicit wait for the response
    input_ = driver.find_element(By.XPATH, '//input[@class={}]'.format('\"' + inputClass + '\"'))
    input_.clear()
    input_.send_keys('{}'.format(Domain.preProcess.categorie[0]) + Keys.ENTER)
    time.sleep(15)
    resultPage = driver.current_url
    return resultPage

a = np.array([1,5,10,13,-9,-7])
b = np.array([[1,3,1,3], [1,4,1,3], [1,4,1,3]])
print(a[[1,1,2,2], [1,3,1,3]])
print(b[1][1])
print(a[[1,3]])
print(a[1,3])