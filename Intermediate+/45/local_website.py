from bs4 import BeautifulSoup

# Beautiful Soup: Parsing HTML and XML

# From File
with open("./website.html", encoding='utf-8') as file:
    website_file = file.read()

# Defining the Beautiful Soup
soup = BeautifulSoup(website_file, 'html.parser')

# The soup object contains the entire html file
# We can get the tags too, and prettify it using prettify

print(soup.p) #find first paragraph
print(soup.find(name="p")) #find first paragraph too, but we cann also specify id and class
print(soup.find_all("p")) #find all paragraph

# Get all anchor text
anchor_tags = soup.find_all("a")

for tag in anchor_tags:
    print(tag.get("href"))
    # Get the attribute inside

# Secify lots of things
heading = soup.find(name= 'h1',id='name')
print(heading)

# for class, it wil be class_ since class is a keyword
print(soup.find_all(name='h3', class_='heading'))

# Use Selectors to specify -> must learn css selectors
link_inside_others = soup.select_one(selector='p a')
print(link_inside_others)

print(soup.select(".heading"))

