from bs4 import BeautifulSoup
import requests
from pprint import pprint

empire_site_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(empire_site_url)
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, 'html.parser')
website_title = soup.find(name='div', class_="article-heading").getText()
movies_list = [movie.getText() for movie in soup.find_all(name="h3", class_='title')[::-1]]


with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
