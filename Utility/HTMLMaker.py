import requests
import time
from random import randint

def htmlMaker(url):
    """Make a standard request"""
    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    html = session.get('{}'.format(url))
    return html

file = open("log.txt", "a",encoding='utf8')
for i in range(0, 20):
    html = htmlMaker("https://www.digikala.com/search/category-mouse/?pageno=1&sortby=4")
    file.writelines("round {} ================================================================================================================================".format(i))
    print("round {} ================================================================================================================================".format(i))
    file.writelines(html.text)
    print(html.text)
    if "var module_hash_id_storage = 1;" not in html.text:
        break

    time.sleep(randint(1,2))