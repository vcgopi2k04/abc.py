import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://www.https://www.oyorooms.com/hotels-in-hyderabad/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find an element by tag name and print its contents
heading = soup.find('h1')
print(heading.text)
