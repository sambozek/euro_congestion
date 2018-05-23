import pandas as pd
import requests

wikipedia_url_of_euro_cities = 'https://en.wikipedia.org/wiki/List_of_metropolitan_areas_in_Europe'
req_of_euro_cities = requests.get(wikipedia_url_of_euro_cities)

euro_cities = pd.read_html(req_of_euro_cities.content, flavor='bs4',header=0)[0]

euro_cities.to_csv('list_of_european_cities.csv')