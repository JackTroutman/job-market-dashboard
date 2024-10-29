from bs4 import BeautifulSoup
import requests
import pandas as pd

# takes web page in html form
html = requests.get('https://www.remotepython.com/jobs/?q=Python').text
soup = BeautifulSoup(html, 'html.parser')

movie_info = {
    'rank':[],
    'peak':[],
    'title':[],
    'gross income':[],
    'year':[],
}

items = soup.find_all('tr')

# Loop to get the country, capita, population, area of each item and store in the dictionary
for item_counter in items:
    print(items)
    #rank = item_counter.find().get_text().strip()
    #peak = item_counter.find().get_text().strip()
    #title = item_counter.find().get_text().strip()
    #gross_income = item_counter.find().get_text().strip()
    #year = item_counter.find().get_text().strip()

    #movie_info["rank"].append(rank)
    #movie_info["peak"].append(peak)
    #movie_info["title"].append(title)
    #movie_info["gross income"].append(gross_income)
    #movie_info["year"].append(year)

# Transform the dictionary into a dataframe
df = pd.DataFrame(movie_info)
df