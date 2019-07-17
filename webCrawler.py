'''
this webcrawler will go into each post link and capture information
'''


import requests
from bs4 import BeautifulSoup

def webCrawler(maxPage):
    page = 1
    while page <= maxPage:
        url = 'https://washingtondc.craigslist.org/search/doc/mca?s=' + str(page)
        sourceCode = requests.get(url) # request.get() connects to the website
        plainText = sourceCode.text # only retreives text data and ignores everything else
        soup = BeautifulSoup(plainText) # formats plainText data so BeautifulSoup can read/sort it
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}): # 'a' is the link code in HTML. class:... you need to research what the webiste is labeling titles
            href = link.get('href')
            title = link.string # this will only store all the text data from link into title; as we want the title text
            print(href)
            print(title)
            singleItem(href)
        page += 1

def singleItem(itemURL):
    sourceCode = requests.get(itemURL)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText)
    for itemName in soup.findAll('span', {'id': 'titletextonly'}):
        print(itemName.string)
    #for link in soup.findAll('a'): # this for loop will print all and any link on the page (reply, about, print, etc)
        #href = link.get('href')
        #print(href)

webCrawler(1)