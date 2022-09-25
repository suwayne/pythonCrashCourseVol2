"""
this project is webscraping football league stats and using this data to

"""

import requests
from bs4 import BeautifulSoup
standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standings_url)
soup = BeautifulSoup(data.text)
standings_table = soup.select("table.stats_table")[0]

links = standings_table.find_all("a")


# print(stadings_table)