import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import html5lib

traffic = pd.read_csv('/Users/sebozek/PycharmProjects/time_spent_in_congestion/hoursspentincongestion.csv')


wikipedia_url_of_euro_cities = 'https://en.wikipedia.org/wiki/List_of_metropolitan_areas_in_Europe'
req_of_euro_cities = requests.get(wikipedia_url_of_euro_cities)
soup = BeautifulSoup(req_of_euro_cities.content, "lxml")


euro_cities = soup.findAll(bgcolor="#CFECEC")

cities_dict = {}
for row in euro_cities:
    cities_dict[row.a.contents[0]] =row.findAll('span')
print(cities_dict)
# df_euro_cities = pd.read_html(euro_cities)
#
# print(df_euro_cities)