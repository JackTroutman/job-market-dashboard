from bs4 import BeautifulSoup
import requests

html = requests.get('https://en.wikipedia.org/wiki/List_of_highest-grossing_films').text

soup = BeautifulSoup(html, 'html.parser')

# allJobs = soup.find_all('div', class_ = 'col-md-11')
Job = soup.find('div', class_ = 'col-md-11')


char = Job.text.strip()
counter = 0
while char != '\n':
    char = Job.text.strip()[counter]
    print(char, end = '')
    counter += 1