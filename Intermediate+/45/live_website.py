# Parsing A Live Website -> use requests

from bs4 import BeautifulSoup
import requests

hacker_news_url = 'https://news.ycombinator.com/'
# scraping hacker_news

# get the text using get request
hacker_news = requests.get(hacker_news_url).text

# Create the soup
soup = BeautifulSoup(hacker_news, "html.parser")

# Use selector
titles = soup.select(".storylink")
subtexts = soup.select(".subtext")
# There are links without upvotes, so it needs to be this way

upvotes = []
for score in subtexts:
    if not score.select_one('.score'):
        upvotes.append(0)
    else:
        upvotes.append(int(score.select_one('.score').get_text().split()[0]))

news = []

for i in range(len(titles)):
    news.append({
        'title':titles[i].get("href"),
        'link':titles[i].get_text(),
        'upvotes':upvotes[i]
    })

print(news)