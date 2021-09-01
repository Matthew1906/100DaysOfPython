from bs4 import BeautifulSoup
from os import getenv
from dotenv import load_dotenv
import requests, re, datetime as dt

load_dotenv()

def check_date(date):
    '''Check if Inserted Data is Valid'''
    date_regex = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
    if not re.search(date_regex, date):
        return False
    temp = list(map(int, date.split('-')))
    try:
        dt.datetime(temp[0], temp[1], temp[2])
    except ValueError:
        return False
    else:
        return True

# Prompt the user to insert date
while True:
    date = input("On which date do you want to travel to? Type the date in the format YYYY-MM-DD!\n>> ").strip()
    if check_date(date):
        break

# Create the URL based on Inputted Date
billboard_url = f'https://www.billboard.com/charts/hot-100/{date}'

# User GET Request to get the text
billboard_response = requests.get(billboard_url).text

# Scrape using Beautiful Soup
billboard_soup = BeautifulSoup(billboard_response, 'html.parser')

# Find tags based on name and class
billboard_titles = billboard_soup.find_all(name= 'span', class_='chart-element__information__song')

# Retrieve the titles and put it into a list
titles = []
for billboard_title in billboard_titles:
    titles.append(billboard_title.get_text())

# Use Spotify API 
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.json",
    ),
)

user_id = sp.current_user()["id"]

song_links = []

for title in titles:
    year = date.split("-")[0]
    link = sp.search(q=f'track:{title} year:{year}', type = 'track', limit = 1)
    if len(link['tracks']['items'])==0:
        continue
    else:
        song_links.append(link['tracks']['items'][0]['uri'])

playlist_id = sp.user_playlist_create(
    user = user_id,
    name = f'{date} Top 100 Billboard Songs',
    public = False,
    description = f'{date} Top 100 Billboard Songs: Web Scraping using Python'
)['id']

sp.playlist_add_items(playlist_id=playlist_id, items=song_links)
print(f'{date} Top 100 Billboard Songs has been created! Check your Spotify Application!')
