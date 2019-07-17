'''
this webscrapper will save into a csv file
'''


from bs4 import BeautifulSoup
import requests
from csv import writer

# input url of webpage
url = 'https://washingtondc.craigslist.org/d/motorcycles-scooters/search/mca'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='result-info')

# creating a csv file to save what I've scrapped
with open('CL_post.csv', 'w') as csv_file:  # the 'as csv_file' is just shorthand notation. think pandas as pd
    csv_writer = writer(csv_file)  # writer was imported already. allows you to 'write'
    headers = ['Title', 'Price', 'Link']  # headers you want as a list
    csv_writer.writerow(headers)  # 'writerow' populates whatever you pass

    for post in posts:
        title = post.find(class_='result-title hdrlnk').get_text()
        price = post.find(class_='result-price').get_text()
        link = post.find('a')['href']
        csv_writer.writerow([title, price, link])  # each row will be populated with title, price, link
        #print(title, price)