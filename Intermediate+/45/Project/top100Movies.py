# Day 45 Project of 100 Days of Code
# Project Name: Top 100 Movies
# Things i implemented: requests, beautiful soup, web scraping

# The program can't work well, since there are some countermeasures i can't exactly counter
# Since i can't extract the H3 (containing the title), i extracted the alt from image, which in some cases don't mention the movie title

import requests
from bs4 import BeautifulSoup

url = 'https://www.empireonline.com/movies/features/best-movies-2/'

movie_page = requests.get(url=url)

soup = BeautifulSoup(movie_page.text, "html.parser")

movie_tags = soup.select('#__next > main > article > div.jsx-2601023975.article-content > .jsx-3821216435.block-item.listicle-container > .listicle-item.jsx-3821216435')[::-1]

movies = []

for movie_tag in movie_tags:
    movies.append(movie_tag.find('img').get("alt"))

for i in range(len(movies)):
    with open('Project/Top 100 Movies.txt', 'a') as file:
        file.write(f'{i+1}. {movies[i]}\n')
