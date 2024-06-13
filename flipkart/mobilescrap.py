#import modules

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

#Scrapping the Data

url = "https://www.flipkart.com/search?q=mobiles"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find_all('div',class_='_4rR01T')
ratings = soup.find_all('div',class_='_3LWZlK')
reviews = soup.find_all('span',class_='_2_R_DZ')
prices = soup.find_all('div',class_='_3I9_wc _27UcVY')

mt = []
mr = []
mre = []
mp = []

for title,rating,rev,price in zip(titles,ratings,reviews,prices):
    mt.append(title.text)
    mr.append(rating.text)
    mre.append(rev.text)
    mp.append(price.text)
    
#saving data in csv

d = {'mobile':mt,'ratings':mr,'reviews':mre,'prices':mp}
model = pd.DataFrame(data=d)

model.to_csv("mobiles-data.csv")