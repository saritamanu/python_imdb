import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

def main():
    response = requests.get(url, headers=headers)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    movietags = soup.select('li.ipc-metadata-list-summary-item')
    movietags0 = movietags[0]
    def getName(movie_tag):
        name_tag = movie_tag.select_one('h3.ipc-title__text')
        moviesplit = name_tag.text.split()
        return moviesplit
    def getYear(movie_tag):
        year_tag = movie_tag.select_one('span.sc-b4f120f6-7')
        moviesplit = year_tag.text.split()
        return moviesplit
    
    names = [getName(tag) for tag in movietags]
    years = [getYear(tag) for tag in movietags]
    
    print(years)




if __name__ == '__main__':
    main()

