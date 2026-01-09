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
    movietagslen = len(movietags)
    def getName(movie_tag):
        name_tag = movie_tag.select_one('h3.ipc-title__text')
        name = name_tag.text
        return name
    def getYear(movie_tag):
        year_tag = movie_tag.select_one('span.sc-b4f120f6-7')
        moviesplit = year_tag.text
        return moviesplit
    def getRating(movie_tag):
        rating_tag = movie_tag.select('span.sc-b4f120f6-7')[2]
        rating = rating_tag.text
        return rating
    
    names = [getName(tag) for tag in movietags]
    years = [getYear(tag) for tag in movietags]
    ratings = [getRating(tag) for tag in movietags]
    
    while True:
        idx=random.randrange(0, movietagslen)
        
        print(f"Movie: {names[idx]}, {years[idx]} - Rating: {ratings[idx]}")
        user_input = input("Do you want another recommendation? (y/[n]): ").strip().lower()
        if user_input != 'y':
            break



if __name__ == '__main__':
    main()

